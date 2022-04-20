from pyexpat import model
from django.db import models

import uuid


# Create your models here.


class Students(models.Model):
    sID = models.UUIDField(blank=False, primary_key=True,
                           default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=20)
    regNumber = models.IntegerField(unique=True)
    password = models.TextField()
    branch = models.CharField(max_length=10)
    dateTimeOfJoin = models.DateTimeField()
    questionRecord = models.JSONField(blank=True, null=True)
    answerRecord = models.JSONField(blank=True, null=True)
    isVerified = models.BooleanField(default=False)


class Teachers(models.Model):
    tID = models.UUIDField(blank=False, primary_key=True,
                           default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=20)
    mailId = models.CharField(max_length=25, unique=True)
    password = models.TextField()
    branch = models.CharField(max_length=10)
    dateTimeOfJoin = models.DateTimeField()
    questionRecord = models.JSONField(blank=True, null=True)
    answerRecord = models.JSONField(blank=True, null=True)
    isVerified = models.BooleanField(default=False)


class Quentions(models.Model):
    qID = models.UUIDField(blank=False, primary_key=True,
                           default=uuid.uuid4, editable=False)
    uID = models.CharField(max_length=36)
    byStudent = models.BooleanField(default=True)
    title = models.CharField(max_length=30)
    about = models.TextField()
    dateTimeOfPost = models.DateTimeField()
    likeCount = models.IntegerField(default=0)
    disLikeCount = models.IntegerField(default=0)
    comments = models.IntegerField(default=0)
    isFixed = models.BooleanField(default=False)
    correntAnswer = models.CharField(max_length=36, blank=True)


class Answers(models.Model):
    aID = models.UUIDField(blank=False, primary_key=True,
                           default=uuid.uuid4, editable=False)
    uID = models.CharField(max_length=36)
    qID = models.CharField(max_length=36, default=None)
    byStudent = models.BooleanField(default=True)
    ans = models.TextField()
    dateTimeOfPost = models.DateTimeField()
    likeCount = models.IntegerField(default=0)
    disLikeCount = models.IntegerField(default=0)
