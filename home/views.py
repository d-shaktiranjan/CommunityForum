from django.shortcuts import render, redirect
from home.models import Answers, Students, Teachers, Quentions
from django.contrib.auth.hashers import make_password, check_password
from datetime import datetime

from home.utils import generateSalt
from home.reaction import giveReaction
# Create your views here.


def index(request):
    try:
        allQuestions = Quentions.objects.all()
        nameList = []
        for item in allQuestions:
            if item.byStudent:
                user = Students.objects.filter(sID=item.uID).first()
            else:
                user = Teachers.objects.filter(tID=item.uID).first()
            nameList.append(user.name)
        sendDict = {
            "post": allQuestions,
            "postNameMix": zip(allQuestions, nameList),
        }
        return render(request, "index.html", sendDict)
    except:
        return render(request, "index.html")


def loginSignup(request):
    if request.session.get("log"):
        return redirect(index)
    return render(request, "loginSignup.html")


def signup(request):
    if request.method == "POST":
        userType = request.POST.get("acc-type")
        name = request.POST.get("name")
        password = request.POST.get("password")
        conPassword = request.POST.get("conPassword")
        branch = request.POST.get("branch")
        uId = request.POST.get("mail")
        regNumber = uId.split("@")[0]
        if password == conPassword:
            if userType == "student":
                newStudent = Students(
                    name=name, regNumber=regNumber, password=make_password(password+generateSalt(uId)), branch=branch, dateTimeOfJoin=datetime.now())
                newStudent.save()
                return alert(request, True, "Your account is created", "Now you can login", "/")
            newTeacher = Teachers(name=name, mailId=uId,
                                  password=make_password(password+generateSalt(uId)), branch="CSE", dateTimeOfJoin=datetime.now())
            newTeacher.save()
            return alert(request, True, "Your account is created", "Now you can login", "/")
        return alert(request, False, "Error", "Password not confirm password not matched.", "/")
    return redirect(index)


def userLogin(request, isStudent, uId, password):
    if isStudent:
        user = Students.objects.filter(regNumber=uId).first()
    else:
        user = Teachers.objects.filter(mailId=uId).first()
    if user is None:
        return alert(request, False, "Signup first", "Create an account to continue", "/")
    if check_password(password, user.password):
        request.session['log'] = True
        if isStudent:
            request.session['uId'] = str(user.sID)
        else:
            request.session['uId'] = str(user.tID)
        request.session['name'] = user.name
        request.session['isStudent'] = isStudent
        return redirect(index)
    return alert(request, False, "Password not matched", "", "/")


def login(request):
    if request.method == "POST":
        userType = request.POST.get("acc-type")
        password = request.POST.get("password")
        mail = request.POST.get("mail")
        isStudent = True if userType == "student" else False
        return userLogin(request, isStudent, mail, password+generateSalt(mail))
    return redirect(index)


def logout(request):
    del request.session['log']
    del request.session['uId']
    del request.session['name']
    del request.session['isStudent']
    return redirect(index)


def postQuestion(request):
    if request.session.get("log"):
        if request.method == "POST":
            title = request.POST.get("title")
            about = request.POST.get("about")
            isStudent = request.session.get("isStudent")
            new = Quentions(title=title, about=about, uID=request.session.get(
                "uId"), byStudent=isStudent, dateTimeOfPost=datetime.now())
            new.save()
            return alert(request, True, "Post added", "Wait for others response", "/")
        return render(request, "postQuestion.html")
    return redirect(loginSignup)


def postComment(request):
    if request.session.get("log"):
        if request.method == "POST":
            about = request.POST.get("about")
            qID = request.POST.get("qID")
            isStudent = request.session.get("isStudent")
            uID = request.session.get("uId")
            newComment = Answers(
                uID=uID, qID=qID, byStudent=isStudent, ans=about, dateTimeOfPost=datetime.now())
            newComment.save()
    return alert(request, True, "Added !", "", f"/postView/{qID}")


def profile(request):
    if request.session.get("log"):
        user = Students.objects.filter(sID=request.session.get("sId")).first()
        myDict = {"user": user}
        questions = Quentions.objects.filter(
            uID=request.session.get("sId")).all()
        myDict["totalQuestions"] = len(questions)
        if len(questions) > 0:
            myDict["questionList"] = questions
        return render(request, "profile.html", myDict)
    return redirect(index)


def postView(request, slug):
    post = Quentions.objects.filter(qID=slug).first()
    if post.byStudent:
        user = Students.objects.filter(sID=post.uID).first()
    else:
        user = Teachers.objects.filter(tID=post.uID).first()
    comments = Answers.objects.filter(qID=slug).all()
    commentUsers = []
    for item in comments:
        if item.byStudent:
            cUser = Students.objects.filter(sID=item.uID).first()
        else:
            cUser = Teachers.objects.filter(tID=item.uID).first()
        commentUsers.append(cUser.name)
    sendDict = {
        "post": post,
        "name": user.name,
        "mixList": zip(comments, commentUsers),
        "slug": slug,
    }
    return render(request, "postView.html", sendDict)


def addLike(request):
    if request.session.get("log"):
        if request.method == "POST":
            contentId = request.POST.get("qID")
            userId = request.session.get('uId')
            isStudent = request.session.get('isStudent')
            status = giveReaction(isStudent, userId, True, contentId, True)
            return redirect(index)
    return redirect(index)


def addDisLike(request):
    if request.session.get("log"):
        if request.method == "POST":
            contentId = request.POST.get("qID")
            userId = request.session.get('uId')
            isStudent = request.session.get('isStudent')
            status = giveReaction(isStudent, userId, True, contentId, False)
            return redirect(index)
    return redirect(index)


def alert(request, isSuccess, msg, about, link):
    myDict = {
        "msg": msg,
        "about": about,
        "link": link,
        "status": "success" if isSuccess else "error"
    }
    return render(request, "alert.html", myDict)
