from django.db import models

# Create your models here.


class StudentData(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=25, unique=True)
    roll = models.CharField(max_length=10, unique=True)
    branch = models.CharField(max_length=10)
    dateOfJoin = models.DateField()
