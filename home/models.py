from django.db import models
from datetime import datetime

# Create your models here.


class Students(models.Model):
    name = models.CharField(max_length=20)
    regNumber = models.IntegerField(primary_key=True)
    password = models.TextField()
    branch = models.CharField(max_length=10)
    dateTimeOfJoin = models.DateTimeField(default=datetime.now())


class Teachers(models.Model):
    name = models.CharField(max_length=20)
    mailId = models.CharField(max_length=25, primary_key=True)
    password = models.TextField()
    branch = models.CharField(max_length=10)
    dateTimeOfJoin = models.DateTimeField(default=datetime.now())
