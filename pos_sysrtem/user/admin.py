from django.contrib import admin
from .models import Institute, Student, Teacher, Profile, ShopOwner


# Register your models here.

@admin.register(Institute)
class InstituteAdmin(admin.ModelAdmin):
    list_display = ('institute_name','contends')


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('user', 'student_ID', 'student_class')


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('user',  'teacher_ID')
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    # teacher_name = models.CharField(max_length=6)
    # teacher_ID = models.CharField(max_length=10)
    # institute = models.ForeignKey(Institute, on_delete=models.DO_NOTHING)
    # contents = models.TextField()


@admin.register(Profile)
class ProFileAdmin(admin.ModelAdmin):
    list_display = ('user', 'real_name', 'is_student', 'is_teacher', 'is_shop_owner')


@admin.register(ShopOwner)
class ShopOwnerAdmin(admin.ModelAdmin):
    list_display = ('user', 'owner_ID')
