from django.http import JsonResponse
from home.models import Students, Teachers
from api.models import OTPData

from django.conf import settings
from django.core.mail import send_mail

from api.utils import otpGenerate
from home.utils import alert


def isUserVerfied(uID, isStudent):
    if isStudent:
        user = Students.objects.filter(sID=uID).first()
    else:
        user = Teachers.objects.filter(tID=uID).first()
    return user.isVerified


def sendOTP(request):
    data = {"name": "Shakti", "status": False}
    if request.session.get("log"):
        uID = request.session.get("uId")
        isStudent = request.session.get("isStudent")
        if isStudent:
            user = Students.objects.filter(sID=uID).first()
            mailID = user.regNumber
        else:
            user = Teachers.objects.filter(tID=uID).first()
            mailID = user.mailId
        OTP = otpGenerate()
        send_mail(
            subject='OTP | CVRCF',
            message=f'Hey {user.name},your OTP is {OTP}',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[f"{mailID}@cgu-odisha.ac.in"]
        )
        otpData = OTPData(uID=uID, OTP=OTP, isStudent=isStudent)
        otpData.save()
        data["status"] = True
        return JsonResponse(data)
    return JsonResponse(data)


def verifyOTP(request):
    if request.method == "POST" and request.session.get("log"):
        isStudent = request.session.get("isStudent")
        uID = request.session.get("uId")
        if isStudent:
            user = Students.objects.filter(sID=uID).first()
        else:
            user = Teachers.objects.filter(tID=uID).first()
        OTPFromUser = request.POST.get("otp")
        findOTP = OTPData.objects.filter(uID=uID).first()
        if OTPFromUser == findOTP.OTP:
            user.isVerified = True
            user.save()
            findOTP.delete()
            return alert(request, True, "You are now verified", "Now your can post & comment", "/profile")
        findOTP.delete()
        return alert(request, False, "OTP not matched", "Try again", "/profile")
    return alert(request, False, "Don't try", "No words for you..", "/")
