from django.shortcuts import render
from .models import Shop

# Create your views here.

def shop_list(request):
    shops = Shop.objects.all


    context = {}
    context['shop_list'] = shops
    return render(request, 'store/shop_list.html', context)
