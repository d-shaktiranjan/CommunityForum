from django.shortcuts import render, redirect
from home.models import Students, Teachers, Quentions
from django.contrib.auth.hashers import make_password, check_password
from datetime import datetime

from home.utils import generateSalt
# Create your views here.


def index(request):
    # return HttpResponse(f"Hey user - {request.session.get('uId')}")
    return render(request, "index.html")


def loginSignup(request):
    return render(request, "loginSignup.html")


def signup(request):
    if request.method == "POST":
        userType = request.POST.get("acc-type")
        name = request.POST.get("name")
        password = request.POST.get("password")
        conPassword = request.POST.get("conPassword")
        uId = request.POST.get("mail")
        regNumber = uId.split("@")[0]
        if password == conPassword:
            if userType == "student":
                newStudent = Students(
                    name=name, regNumber=regNumber, password=make_password(password+generateSalt(uId)), branch="CSE", dateTimeOfJoin=datetime.now())
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
    return redirect(index)


def postQuestion(request):
    if request.session.get("log"):
        if request.method == "POST":
            title = request.POST.get("title")
            about = request.POST.get("about")
            new = Quentions(title=title, about=about, uID=request.session.get(
                "sId"), dateTimeOfPost=datetime.now())
            new.save()
            return alert(request, True, "Post added", "Wait for others response", "/")
        return render(request, "postQuestion.html")
    return redirect(index)


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


def alert(request, isSuccess, msg, about, link):
    myDict = {
        "msg": msg,
        "about": about,
        "link": link,
        "status": "success" if isSuccess else "error"
    }
    return render(request, "alert.html", myDict)
