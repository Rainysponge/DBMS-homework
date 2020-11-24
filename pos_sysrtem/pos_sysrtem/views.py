from django.shortcuts import render
from user.models import Institute



def home(request):
    institude = Institute.objects.all()
    context = {}
    context['institude'] = institude
    return render(request, 'index.html', context)
