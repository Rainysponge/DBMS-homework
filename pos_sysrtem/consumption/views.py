import datetime
from django.shortcuts import render
from django.utils import timezone
from django.db.models import Sum
from django.contrib.auth.models import User
from store.models import Pay
from .utils import get_seven_days_consumption_data


# Create your views here.

def student_consumption(request):
    user = request.user
    dates, seven_days_consumption = get_seven_days_consumption_data(user)

    pay_list = Pay.objects.filter(buyer_id=user)
    context = {}
    # context['pay_today'] = pay_today
    context['pay_list'] = pay_list
    context['dates'] = dates
    context['seven_days_consumption'] = seven_days_consumption
    return render(request, 'consumption/student_consumption.html', context)

