from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import StudentData
# Create your views here.


def index(request):
    return HttpResponse("POST Home page")


@csrf_exempt
def addStudent(request):
    if request.method == "POST":
        status = False
        name = request.POST.get("name")
        email = request.POST.get("email")
        roll = request.POST.get("roll")
        branch = request.POST.get("branch")
        dateOfJoin = "2021-09-03"
        data = {
            "email": email,
            "status": status,
        }
        newStudent = StudentData(
            name=name, email=email, roll=roll, branch=branch, dateOfJoin=dateOfJoin)
        newStudent.save()
        data["status"] = True
        return JsonResponse(data)
    return HttpResponse("GET method is not allowed")
