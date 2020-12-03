from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib import auth
from django.contrib.auth.models import User
# from django.contrib.auth.models import User
from .forms import LoginFrom, RegForm
from .models import Profile

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
            elif who == '学生':
                profile = Profile.objects.create(user=user, real_name=real_name, is_student=True)
            else:
                profile = Profile.objects.create(user=user, real_name=real_name, is_shop_owner=True)
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
