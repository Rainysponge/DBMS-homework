from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Institute(models.Model):
    institute_name = models.CharField(max_length=16)
    contends = models.TextField()


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    real_name = models.CharField(max_length=6, null=True, blank=True)
    sex = models.CharField(max_length=2, null=True, blank=True)
    IDnumber = models.CharField(max_length=20, null=True, blank=True)
    birth = models.DateTimeField(null=True, blank=True)
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    is_shop_owner = models.BooleanField(default=False)


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # student_name = models.CharField(max_length=6, null=True, blank=True)
    student_ID = models.CharField(max_length=10, null=True, blank=True)
    institute = models.ForeignKey(Institute, on_delete=models.DO_NOTHING, null=True, blank=True)
    student_class = models.CharField(max_length=20, null=True, blank=True)
    
    dept = models.CharField(max_length=10, null=True, blank=True)
    
    contents = models.TextField()


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # teacher_name = models.CharField(max_length=6, null=True, blank=True)
    teacher_ID = models.CharField(max_length=10, null=True, blank=True)


class ShopOwner(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # owner_name = models.CharField(max_length=6, null=True, blank=True)
    owner_ID = models.CharField(max_length=10, null=True, blank=True)



def get_Profile(self):
    if Profile.objects.filter(user=self).exists():
        profile = Profile.objects.get(user=self)
        return profile
    else:
        return ''

User.Profile = get_Profile