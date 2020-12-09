from django.shortcuts import render
from django.contrib.auth.models import User
from user.models import Institute, Profile
from store.models import Shop


def home(request):

    # shop_list =
    context = {}
    # profile = Profile.objects.get(user=user)
    # if profile.is_shop_owner:
    #     shop_list = Shop.objects.filter(shop_owner=user)
    #     context['shop_list'] = shop_list
    institude = Institute.objects.all()
    user = request.user


    context['institude'] = institude
    context['user_type'] = type(user)
    return render(request, 'index.html', context)
