import datetime
from django.utils import timezone
from django.db.models import Sum
from .models import Pay, Commodity, Order


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


def get_commodity_consumption_data(shop):
    commodity_list = []
    pay_money = []
    res = []
    count = 0
    # pay_today = Pay.objects.filter(buyer_id=user, pay_time__year=today.year,
    #                                pay_time__month=today.month, pay_time__day=today.day)
    try:
        commodity = Commodity.objects.filter(shop=shop)
    except:
        return commodity_list, pay_money
    for item in commodity:
        commodity_list.append(item.commodity_name)
        try:
            order_detail = Order.objects.filter(commodity_id=item)
        except:
            result = 0
            pay_money.append(result)
            continue

        number_sum = order_detail.aggregate(number_sum=Sum('number'))
        result = number_sum['number_sum'] * item.commodity_price if number_sum['number_sum'] else 0
        pay_money.append(result)
        res.append({'value': result, 'name': item.commodity_name})

    if len(res) <= 3:
        return res
    else:
        res = sorted(res, key=lambda x: x['value'], reverse=True)
        return res[:3]
