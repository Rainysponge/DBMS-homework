import datetime
from django.utils import timezone
from django.db.models import Sum
from .models import Pay


def get_30_days_earn_data(shop):
    today = timezone.now().date()

    pay_money = []
    dates = []
    for i in range(30, -1, -1):
        date = today - datetime.timedelta(days=i)
        dates.append(date.strftime('%m/%d'))
        pay_details = Pay.objects.filter(shop=shop, pay_time__year=date.year,
                                         pay_time__month=date.month, pay_time__day=date.day)
        result = pay_details.aggregate(pay_details_sum=Sum('pay_money'))
        pay_money.append(result['pay_details_sum'] or 0)

    return dates, pay_money
