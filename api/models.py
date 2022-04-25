from django.db import models


class OTPData(models.Model):
    uID = models.CharField(max_length=36)
    OTP = models.CharField(max_length=10)
    isStudent = models.BooleanField()
