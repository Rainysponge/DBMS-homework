from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Institute(models.Model):
    institute_name = models.CharField(max_length=16)
    contends = models.TextField()


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    student_name = models.CharField(max_length=6)
    student_ID = models.CharField(max_length=10)
    institute = models.ForeignKey(Institute, on_delete=models.DO_NOTHING)
    student_class = models.CharField(max_length=20)
    sex = models.CharField(max_length=2)
    dept = models.CharField(max_length=10)
    birth = models.DateTimeField(null=True, blank=True)
    contents = models.TextField()


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    teacher_name = models.CharField(max_length=6)
    teacher_ID = models.CharField(max_length=10)
