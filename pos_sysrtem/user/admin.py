from django.contrib import admin
from .models import Institute, Student, Teacher


# Register your models here.

@admin.register(Institute)
class InstituteAdmin(admin.ModelAdmin):
    list_display = ('institute_name','contends')


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('user', 'student_name', 'student_ID', 'student_class')


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('user', 'teacher_name', 'teacher_ID')
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    # teacher_name = models.CharField(max_length=6)
    # teacher_ID = models.CharField(max_length=10)
    # institute = models.ForeignKey(Institute, on_delete=models.DO_NOTHING)
    # contents = models.TextField()
