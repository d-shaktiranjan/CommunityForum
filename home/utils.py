from home.models import Students, Teachers
from django.shortcuts import render


def generateSalt(mail):
    salt = "@"
    salt += mail[::2]+"#"
    salt += mail[-3:]+"&"
    return salt


def isNewUser(id, isStudent):
    if isStudent:
        user = Students.objects.filter(regNumber=id).first()
    else:
        user = Teachers.objects.filter(mailId=id).first()
    return user == None


def alert(request, isSuccess, msg, about, link):
    myDict = {
        "msg": msg,
        "about": about,
        "link": link,
        "status": "success" if isSuccess else "error"
    }
    return render(request, "alert.html", myDict)


def isUserVerified(request):
    userID = request.session.get("uId")
    isStudent = request.session.get("isStudent")
    if isStudent:
        user = Students.objects.filter(sID=userID).first()
    else:
        user = Teachers.objects.filter(tID=userID).first()
    print(user.isVerified)
    return user.isVerified
