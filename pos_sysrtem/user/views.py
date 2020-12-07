from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib import auth
from django.contrib.auth.models import User
# from django.contrib.auth.models import User
from .forms import LoginFrom, RegForm, changeStudentInfoForm, changeTeacherInfoForm, changeShopownerInfoForm
from .models import Profile, Student, Teacher, ShopOwner


# Create your views here.


def login(request):
    if request.method == 'POST':
        login_form = LoginFrom(request.POST)
        if login_form.is_valid():
            user = login_form.cleaned_data['user']
            auth.login(request, user)
            context = {'log_massage': request.GET.get('from')}
            # return redirect(request.GET.get('from', reverse('home')))
            return render(request, 'index.html', context)
    else:
        login_form = LoginFrom()

    context = {}
    # context['page_title'] = '欢迎'
    context['login_form'] = login_form
    context['form_title'] = '登录'
    return render(request, 'user/login.html', context)


def register(request):
    if request.method == 'POST':
        reg_form = RegForm(request.POST)
        if reg_form.is_valid():
            username = reg_form.cleaned_data['username']
            email = reg_form.cleaned_data['email']
            password = reg_form.cleaned_data['password']
            # school = reg_form.changed_data['school']
            user = User.objects.create_user(username, email, password)  # 创建用户
            real_name = reg_form.cleaned_data['real_name']
            sex = reg_form.cleaned_data['sex']
            who = reg_form.cleaned_data['who']
            # nickname = reg_form.cleaned_data['nickname']
            # 这个地方就是有病
            # grade = reg_form.cleaned_data['grade']
            # student_ID = reg_form.cleaned_data['student_ID']
            user.save()
            if who == '教师':
                profile = Profile.objects.create(user=user, real_name=real_name, is_teacher=True)
                teacher = Teacher.objects.create(user=user)
                teacher.save()
            elif who == '学生':
                profile = Profile.objects.create(user=user, real_name=real_name, is_student=True)
                student = Student.objects.create(user=user)
                student.save()
            else:
                profile = Profile.objects.create(user=user, sex=sex, real_name=real_name, is_shop_owner=True)
                shop_owner = ShopOwner.objects.create(user=user)
                shop_owner.save()
            profile.save()

            user = auth.authenticate(username=username, password=password)
            auth.login(request, user)
            return render(request, 'index.html', {'massage': '恭喜你已经成功注册啦'})
    else:
        reg_form = RegForm()

    context = {}
    context['reg_form'] = reg_form
    context['form_title'] = '注册'
    return render(request, 'user/register.html', context)


def logout(request):
    auth.logout(request)
    return redirect(request.GET.get('from', reverse('home')))


def changeStudentInfo(request, user_pk):
    user = User.objects.get(pk=user_pk)
    if request.method == 'POST':
        change_student_info_form = changeStudentInfoForm(request.POST)
        if change_student_info_form.is_valid():
            pass
            grade = change_student_info_form.cleaned_data['grade']

            dept = change_student_info_form.cleaned_data['dept']

            birth = change_student_info_form.cleaned_data['birth']
            profile = Profile.objects.get(user=user)
            profile.birth = birth

            if Student.objects.get(user=user):
                student = Student.objects.get(user=user)
                student.dept = dept
                student.grade = grade
            else:
                student = Student.objects.create(dept=dept, grade=grade)
            student.save()
            profile.save()
            return render(request, 'index.html', {'massage': '恭喜你已经成功修改学生信息啦'})

    else:
        change_student_info_form = changeStudentInfoForm()

    context = {}

    context['change_student_info_form'] = change_student_info_form
    context['form_title'] = '修改学生信息'
    context['user_name'] = user.username
    context['massege'] = '信息修改成功！'
    return render(request, 'user/change_student_info.html', context)

def changeTeacherInfo(request, user_pk):
    user = User.objects.get(pk=user_pk)
    if request.method == 'POST':
        change_teacher_info_form = changeTeacherInfoForm(request.POST)
        if change_teacher_info_form.is_valid():
            pass

            dept = change_teacher_info_form.cleaned_data['dept']

            birth = change_teacher_info_form.cleaned_data['birth']
            profile = Profile.objects.get(user=user)
            profile.birth = birth

            if Teacher.objects.get(user=user):
                teacher = Teacher.objects.get(user=user)
                teacher.dept = dept
            else:
                teacher = Teacher.objects.create(dept=dept)

            teacher.save()
            profile.save()
            return render(request, 'index.html', {'massage': '恭喜你已经成功修改教师信息啦'})

    else:
        change_teacher_info_form = changeTeacherInfoForm()

    context = {}

    context['change_teacher_info_form'] = change_teacher_info_form
    context['form_title'] = '修改老师信息'
    context['user_name'] = user.username
    context['massege'] = '信息修改成功！'
    return render(request, 'user/change_teacher_info.html', context)


def changeShopownerInfo(request, user_pk):
    user = User.objects.get(pk=user_pk)
    if request.method == 'POST':
        change_shopowner_info_form = changeShopownerInfoForm(request.POST)
        if change_shopowner_info_form.is_valid():
            pass

            IDnumber = change_shopowner_info_form.cleaned_data['IDnumber']

            birth = change_shopowner_info_form.cleaned_data['birth']
            profile = Profile.objects.get(user=user)
            profile.birth = birth

            if ShopOwner.objects.get(user=user):
                shopowner = ShopOwner.objects.get(user=user)
                shopowner.IDnumber = IDnumber

            else:
                shopowner = ShopOwner.objects.create(IDnumber=IDnumber)
            shopowner.save()
            profile.save()
            return render(request, 'index.html', {'massage': '恭喜你已经成功修改商家信息啦'})

    else:
        change_shopowner_info_form = changeShopownerInfoForm()

    context = {}

    context['change_shopowner_info_form'] = change_shopowner_info_form
    context['form_title'] = '修改商家信息'
    context['user_name'] = user.username
    context['massege'] = '信息修改成功！'
    return render(request, 'user/change_shopowner_info.html', context)
