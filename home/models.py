from django.db import models
from datetime import datetime

import uuid


# Create your models here.


class Students(models.Model):
    sID = models.UUIDField(blank=False, primary_key=True,
                           default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=20)
    regNumber = models.IntegerField(unique=True)
    password = models.TextField()
    branch = models.CharField(max_length=10)
    dateTimeOfJoin = models.DateTimeField(default=datetime.now())


class Teachers(models.Model):
    tID = models.UUIDField(blank=False, primary_key=True,
                           default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=20)
    mailId = models.CharField(max_length=25, unique=True)
    password = models.TextField()
    branch = models.CharField(max_length=10)
    dateTimeOfJoin = models.DateTimeField(default=datetime.now())


class Quentions(models.Model):
    qID = models.UUIDField(blank=False, primary_key=True,
                           default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=30)
    about = models.TextField()
    dateTimeOfPost = models.DateTimeField(default=datetime.now())
    likeCount = models.IntegerField(default=0)
    disLikeCount = models.IntegerField(default=0)


class Answers(models.Model):
    aID = models.UUIDField(blank=False, primary_key=True,
                           default=uuid.uuid4, editable=False)
    ans = models.TextField()
    dateTimeOfPost = models.DateTimeField(default=datetime.now())
    likeCount = models.IntegerField(default=0)
    disLikeCount = models.IntegerField(default=0)
