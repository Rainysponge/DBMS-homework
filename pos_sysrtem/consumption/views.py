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
    # today = timezone.now().date()
    # dates = []
    # pay_money = []
    # pay_today = Pay.objects.filter(buyer_id=user, pay_time__year=today.year,
    #                                pay_time__month=today.month,pay_time__day=today.day)
    # for i in range(6, -1, -1):
    #     date = today - datetime.timedelta(days=i)
    #     dates.append(date.strftime('%m/%d'))
    #     pay_details = Pay.objects.filter(buyer_id=user, pay_time=date)
    #     result = pay_details.aggregate(pay_details_sum=Sum('pay_money'))
    #     pay_money.append(result['pay_details_sum'] or 0)
    # now =
    context = {}
    # context['pay_today'] = pay_today
    context['pay_list'] = pay_list
    context['dates'] = dates
    context['seven_days_consumption'] = seven_days_consumption
    return render(request, 'consumption/student_consumption.html', context)

