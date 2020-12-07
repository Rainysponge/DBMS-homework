from django.shortcuts import render
from .models import Shop, Commodity, Order, CommodityToshop
from .forms import createOrderForm


# Create your views here.

def shop_list(request):
    shops = Shop.objects.all

    context = {}
    context['shop_list'] = shops
    return render(request, 'store/shop_list.html', context)


def create_orders(request):
    # user = request.user
    if request.method == 'POST':
        create_order_form = createOrderForm(request.POST)
        if create_order_form.is_valid():
            commodity = create_order_form.cleaned_data['commodity']
            # commodityO = Commodity.objects.get()
            commodityO = Commodity.objects.get(commodity_name=commodity)
            number = create_order_form.cleaned_data['number']
            number = int(number)
            order = Order.objects.create(commodity_id=commodityO, number=number)
            order.save()
            # auth.login(request, user)
            context = {'massage': 'Success'}
            # return redirect(request.GET.get('from', reverse('home')))
            return render(request, 'index.html', context)
    else:
        create_order_form = createOrderForm()
    # shop = Shop.objects.get(shop_owner=user)
    # commodity_list = CommodityToshop.objects.filter(shop_owner=shop)
    # commodity_list = Commodity.objects.filter()
    context = {}
    # context['page_title'] = '欢迎'
    context['create_order_form'] = create_order_form
    # context['commodity_list'] = commodity_list
    context['form_title'] = '##'
    return render(request, 'store/create_orders.html', context)
