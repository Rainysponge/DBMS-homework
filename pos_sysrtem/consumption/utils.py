import datetime
from django.utils import timezone
from django.db.models import Sum
from store.models import Pay, Commodity


def get_seven_days_consumption_data(user):
    today = timezone.now().date()
    dates = []
    pay_money = []
    # pay_today = Pay.objects.filter(buyer_id=user, pay_time__year=today.year,
    #                                pay_time__month=today.month, pay_time__day=today.day)
    for i in range(6, -1, -1):
        date = today - datetime.timedelta(days=i)
        dates.append(date.strftime('%m/%d'))
        pay_details = Pay.objects.filter(buyer_id=user, pay_time__year=date.year,
                                         pay_time__month=date.month, pay_time__day=date.day)
        result = pay_details.aggregate(pay_details_sum=Sum('pay_money'))
        pay_money.append(result['pay_details_sum'] or 0)

    return dates, pay_money



