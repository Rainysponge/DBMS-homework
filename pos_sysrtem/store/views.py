from django.shortcuts import render
from django.contrib.auth.models import User
from user.models import Teacher, Student
from .models import Shop, Commodity, Order, CommodityToshop, Pay
from .forms import createOrderForm, createPayForm, createShopForm, createCommodityForm, updateCommodityForm
from .utils import get_30_days_earn_data, get_commodity_consumption_data
from django.core.paginator import Paginator


# Create your views here.
def myshopList(request):
    try:
        user = request.user
    except:
        return render(request, 'user/login.html', {'massage': '用户未登录！'})
    my_shop_list = Shop.objects.filter(shop_owner=user)

    context = {}

    context['my_shop_list'] = my_shop_list
    return render(request, 'store/myShopList.html', context)
    # pay_list = Pay.objects.filter()


def shop_list(request):
    shops = Shop.objects.all

    context = {}
    context['shop_list'] = shops
    return render(request, 'store/shop_list.html', context)


def create_orders(request, shop_pk):
    user = request.user
    if request.method == 'POST':
        create_order_form = createOrderForm(request.POST)
        if create_order_form.is_valid():

            commodity = create_order_form.cleaned_data['commodity']
            pay_No = create_order_form.cleaned_data['pay_No']
            # shop_id = create_order_form.cleaned_data['shop_id']
            # shop_id = str(user.pk) + '_' + shop_id
            try:
                shop = Shop.objects.get(pk=shop_pk)
            except:
                create_order_form = createOrderForm()
                context = {}
                context['create_order_form'] = create_order_form
                context['form_title'] = '##'
                context['massage'] = '店铺编号有误'
                return render(request, 'store/create_orders.html', context)
            # shop = Shop.objects.get(pk=shop_pk)
            pay_No = str(shop.shop_id) + ':' + pay_No
            pay = Pay.objects.get(pay_No=pay_No)
            commodityO = Commodity.objects.get(commodity_name=commodity, shop=shop)
            try:

                number = create_order_form.cleaned_data['number']
                number = int(number)
                order = Order.objects.create(commodity_id=commodityO, number=number, pay=pay)

                pay.pay_money += commodityO.commodity_price * number
                order.save()
                pay.save()
            except Exception as e:
                create_order_form = createOrderForm()
                context = {}
                context['create_order_form'] = create_order_form
                context['form_title'] = '##'
                context['massage'] = '请输入正确信息'
                return render(request, 'store/create_orders.html', context)

            context = {'massage': 'Success'}
            create_order_form = createOrderForm()
            context['create_order_form'] = create_order_form
            return render(request, 'store/create_orders.html', context)
    else:
        create_order_form = createOrderForm()

    context = {}

    context['create_order_form'] = create_order_form

    context['form_title'] = '##'
    return render(request, 'store/create_orders.html', context)


def creat_pay(request, shop_pk):
    # str
    # user = request.user
    if request.method == 'POST':
        create_pay_form = createPayForm(request.POST)
        if create_pay_form.is_valid():
            # shop = Shop.objects.get(shop_owner=user)
            # shop_id = create_pay_form.cleaned_data['shop_id']
            # shop_id = str(user.pk) + '_' + shop_id
            try:
                shop = Shop.objects.get(pk=shop_pk)
            except:
                create_order_form = createOrderForm()
                context = {}
                context['create_order_form'] = create_order_form
                context['form_title'] = '##'
                context['massage'] = '店铺编号有误'
                return render(request, 'store/create_pay.html', context)
            shop_id = shop.shop_id
            buyer_id = create_pay_form.cleaned_data['buyer_id']
            pay_No = create_pay_form.cleaned_data['pay_No']
            pay_No = str(shop_id) + ':' + pay_No
            try:
                # 验证编号是否已经存在
                payTest = Pay.objects.get(pay_No=pay_No)
                create_pay_form = createPayForm()
                context = {}
                context['create_pay_form'] = create_pay_form
                # context['commodity_list'] = commodity_list
                context['form_title'] = '##'
                context['massage'] = '该编号已经存在！'
                return render(request, 'store/create_pay.html', context)
            except:
                pass
            try:
                student = Student.objects.get(student_ID=buyer_id)
                user_buy = User.objects.get(pk=student.user.pk)
                pay = Pay.objects.create(shop=shop, buyer_id=user_buy, pay_No=pay_No)
                pay.save()
            except Exception as e:
                create_pay_form = createPayForm()
                context = {}
                context['create_pay_form'] = create_pay_form
                # context['commodity_list'] = commodity_list
                context['form_title'] = '##'
                context['massage'] = '请输入正确信息'
                return render(request, 'store/create_pay.html', context)

            context = {'massage': 'Success'}
            create_pay_form = createPayForm()
            context['create_pay_form'] = create_pay_form
            # return redirect(request.GET.get('from', reverse('home')))
            return render(request, 'store/create_pay.html', context)
    else:
        create_pay_form = createPayForm()
    context = {}
    # context['page_title'] = '欢迎'
    context['create_pay_form'] = create_pay_form
    # context['commodity_list'] = commodity_list
    context['form_title'] = '##'
    return render(request, 'store/create_pay.html', context)


def create_shop(request):
    # shop_id
    # shop_name
    # phone_number

    try:
        user = request.user
    except:
        return render(request, 'user/login.html', {'massage': '用户未登录！'})
    if request.method == 'POST':
        create_shop_form = createShopForm(request.POST)
        if create_shop_form.is_valid():
            shop_name = create_shop_form.cleaned_data['shop_name']
            shop_id = create_shop_form.cleaned_data['shop_id']
            phone_number = create_shop_form.cleaned_data['phone_number']
            shop_id = str(user.pk) + '_' + shop_id

            try:
                shopTest1 = Shop.objects.get(shop_id=shop_id)

                create_shop_form = createShopForm()
                context = {}
                context['create_shop_form'] = create_shop_form
                # context['commodity_list'] = commodity_list
                context['form_title'] = '##'
                context['massage'] = '该商店已经存在！'
                return render(request, 'store/create_shop.html', context)
            except:
                pass
            try:
                shopTest2 = Shop.objects.get(shop_name=shop_name)  # 避免重名

                create_shop_form = createShopForm()
                context = {}
                context['create_shop_form'] = create_shop_form
                # context['commodity_list'] = commodity_list
                context['form_title'] = '##'
                context['massage'] = '该商店已经存在！'
                return render(request, 'store/create_shop.html', context)
            except:
                pass
            shop = Shop.objects.create(shop_owner=user, shop_name=shop_name, shop_id=shop_id, phone_number=phone_number)
            shop.save()
            context = {'massage': 'Success'}
            # return redirect(request.GET.get('from', reverse('home')))
            return render(request, 'index.html', context)
    else:
        create_shop_form = createShopForm()
    context = {}
    # context['page_title'] = '欢迎'
    context['create_shop_form'] = create_shop_form
    # context['commodity_list'] = commodity_list
    context['form_title'] = '##'
    return render(request, 'store/create_shop.html', context)


def create_commodity(request, shop_pk):
    try:
        user = request.user
        shop = Shop.objects.get(pk=shop_pk)
    except:
        return render(request, 'user/login.html', {'massage': '用户未登录！'})
    if request.method == 'POST':
        create_commodity_form = createCommodityForm(request.POST)
        # 创建商品
        # update_commodity_form = updateCommodityForm(request.POST)
        if create_commodity_form.is_valid():
            # shop_id = create_commodity_form.cleaned_data['shop_id']

            commodity_price = create_commodity_form.cleaned_data['commodity_price']
            commodity_name = create_commodity_form.cleaned_data['commodity_name']

            try:
                commodity = Commodity.objects.get(shop=shop, commodity_name=commodity_name)
                # update_commodity_form = updateCommodityForm()
                create_commodity_form = createCommodityForm()
                context = {}
                context['create_commodity_form'] = create_commodity_form
                context['form_title'] = '##'
                context['massage'] = '该商品已被创建或存在同名商品！'
                # context['update_commodity_form'] = update_commodity_form
                return render(request, 'store/update_commodity.html', context)
            except:
                pass
            try:

                commodity = Commodity.objects.create(shop=shop, commodity_name=commodity_name,
                                                     commodity_price=commodity_price)
                commodity.save()
            except Exception as e:
                create_commodity_form = createCommodityForm()
                # update_commodity_form = updateCommodityForm()
                context = {}
                context['create_commodity_form'] = create_commodity_form
                # context['update_commodity_form'] = update_commodity_form
                context['form_title'] = '##'
                context['massage'] = '请输入正确信息'
                return render(request, 'store/update_commodity.html', context)

            context = {'massage': '创建商品成功！'}
            create_commodity_form = createCommodityForm()
            context['create_commodity_form'] = create_commodity_form
            return render(request, 'store/update_commodity.html', context)


    else:
        create_commodity_form = createCommodityForm()
        # update_commodity_form = updateCommodityForm()


    context = {}
    # context['page_title'] = '欢迎'
    context['create_commodity_form'] = create_commodity_form
    # context['update_commodity_form'] = update_commodity_form
    # context['commodity_list'] = commodity_list
    context['form_title'] = '##'
    return render(request, 'store/update_commodity.html', context)


def shop_info(request, shop_pk):
    shop_info_list = Shop.objects.get(pk=shop_pk)
    commodity_list = Commodity.objects.filter(shop=shop_info_list)
    paginator = Paginator(commodity_list, 1)  # 每2页进行分页
    page_num = request.GET.get('page', 1)
    page_of_commodity = paginator.get_page(page_num)

    pay_list = Pay.objects.filter(shop=shop_info_list)
    paginator1 = Paginator(pay_list, 1)  # 每2页进行分页
    page_num1 = request.GET.get('page1', 1)
    page_of_pay = paginator1.get_page(page_num1)

    context = {}
    context['shop_info_list'] = shop_info_list
    context['commodity_list'] = page_of_commodity
    context['pay_list'] = page_of_pay
    return render(request, 'store/shop_info.html', context)


def orders_in_pay(request, pay_pk):
    pay = Pay.objects.get(pk=pay_pk)
    order_list = Order.objects.filter(pay=pay)
    context = {'order_list': order_list}
    return render(request, 'store/orders_in_pay.html', context)


def shop_info_with_charts(request, shop_pk):
    shop_info_list = Shop.objects.get(pk=shop_pk)
    dates, earn = get_30_days_earn_data(shop_info_list)
    res = get_commodity_consumption_data(shop_info_list)
    pay_list = Pay.objects.filter(shop=shop_info_list)

    context = {}
    context['shop_info_list'] = shop_info_list
    # context['commodity_list'] = commodity_list
    # context['pay_money'] = pay_money
    context['get_commodity_consumption_data'] = res
    context['dates'] = dates
    context['earn'] = earn
    context['max_earn'] = max(earn)
    context['pay_list'] = pay_list
    return render(request, 'store/shop_info_with_charts.html', context)


def update_commodity_price(request, shop_pk):
    try:
        user = request.user
        shop = Shop.objects.get(pk=shop_pk)
    except:
        return render(request, 'user/login.html', {'massage': '用户未登录！'})
    if request.method == 'POST':
        update_commodity_form = updateCommodityForm(request.POST)
        # 创建商品
        # update_commodity_form = updateCommodityForm(request.POST)
        if update_commodity_form.is_valid():
            # shop_id = create_commodity_form.cleaned_data['shop_id']

            commodity_price = update_commodity_form.cleaned_data['commodity_price']
            commodity_name = update_commodity_form.cleaned_data['commodity_name']

            try:
                commodity = Commodity.objects.get(shop=shop, commodity_name=commodity_name)
                # update_commodity_form = updateCommodityForm()

            except:
                update_commodity_form = updateCommodityForm()
                context = {}
                context['update_commodity_form'] = update_commodity_form
                context['form_title'] = '##'
                context['massage'] = '该商品还未被创建！'
                # context['update_commodity_form'] = update_commodity_form
                return render(request, 'store/update_commodity_price.html', context)
            try:

                commodity.commodity_price = commodity_price
                commodity.save()
            except Exception as e:
                update_commodity_form = updateCommodityForm()
                context = {}
                context['update_commodity_form'] = update_commodity_form
                context['form_title'] = '##'
                context['massage'] = '输入信息有误！'
                # context['update_commodity_form'] = update_commodity_form
                return render(request, 'store/update_commodity_price.html', context)

            context = {'massage': '创建商品成功！'}
            update_commodity_form = updateCommodityForm()
            context['update_commodity_form'] = update_commodity_form
            return render(request, 'store/update_commodity_price.html', context)


    else:
        create_commodity_form = createCommodityForm()
        # update_commodity_form = updateCommodityForm()


    context = {}
    # context['page_title'] = '欢迎'
    update_commodity_form = updateCommodityForm()
    context['update_commodity_form'] = update_commodity_form
    # context['update_commodity_form'] = update_commodity_form
    # context['commodity_list'] = commodity_list
    context['form_title'] = '##'
    return render(request, 'store/update_commodity_price.html', context)
