from home.models import Students, Teachers
from django.shortcuts import render

from os import listdir


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
    return user.isVerified


def isPostImage(postID):
    postID = str(postID)
    about = {"isPic": False, "fileName": ""}
    fileList = listdir("static/postImages")
    postList = []
    for file in fileList:
        tempList = file.split(".")
        postList.append(tempList[0])
    if postID in postList:
        about["isPic"] = True
        about["fileName"] = fileList[postList.index(postID)]
    print(about)
    return about
