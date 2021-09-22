from django.shortcuts import render, redirect
# Create your views here.


def index(request):
    return redirect(signup)


def signup(request):
    if request.method == "POST":
        userType = request.POST.get("type")
        name = request.POST.get("name")
        password = request.POST.get("password")
        conPassword = request.POST.get("conPassword")
        print(f"{name} is a {userType}")
    return render(request, "signup.html")


def login(request):
    return render(request, "login.html")
