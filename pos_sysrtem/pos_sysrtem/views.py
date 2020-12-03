from django.shortcuts import render
from django.contrib.auth.models import User
from user.models import Institute, Profile




def home(request):
    institude = Institute.objects.all()
    user = request.user
    context = {}
    context['institude'] = institude
    context['user_type'] = type(user)
    return render(request, 'index.html', context)
