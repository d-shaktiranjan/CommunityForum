from django.shortcuts import render, redirect, HttpResponse
from home.models import Students, Teachers
# Create your views here.


def index(request):
    return redirect(signup)


def signup(request):
    if request.method == "POST":
        userType = request.POST.get("type")
        name = request.POST.get("name")
        password = request.POST.get("password")
        conPassword = request.POST.get("conPassword")
        uId = request.POST.get("uId")
        if password == conPassword:
            if userType == "student":
                newStudent = Students(
                    name=name, regNumber=uId, password=password, branch="")
                newStudent.save()
                return HttpResponse(f"{name} is a student added")
            newTeacher = Teachers(name=name, mailId=uId,
                                  password=password, branch="")
            newTeacher.save()
            return HttpResponse(f"{name} is a Teacher added")
    return render(request, "signup.html")


def login(request):
    if request.method == "POST":
        userType = request.POST.get("type")
        password = request.POST.get("pass")
        mail = request.POST.get("mail")
        uId = str(mail).split("@")
        if userType == "student":
            student = Students.objects.filter(regNumber=uId[0]).first()
            if student is None:
                return HttpResponse("Sign up first")
            if password == student.password:
                return HttpResponse("Password Correct")
            return HttpResponse("In correct pass")
        teacher = Teachers.objects.filter(mailId=uId[0]).first()
        if teacher is None:
            return HttpResponse("Please signup")
        if password == teacher.password:
            return HttpResponse("Correct Password")
        return HttpResponse("Pass not match")
    return render(request, "login.html")
