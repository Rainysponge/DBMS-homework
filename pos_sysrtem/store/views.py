from django.shortcuts import render
from django.contrib.auth.models import User
from user.models import Teacher, Student
from .models import Shop, Commodity, Order, CommodityToshop, Pay
from .forms import createOrderForm, createPayForm


# Create your views here.

def shop_list(request):
    shops = Shop.objects.all

    context = {}
    context['shop_list'] = shops
    return render(request, 'store/shop_list.html', context)


def create_orders(request):
    user = request.user
    if request.method == 'POST':
        create_order_form = createOrderForm(request.POST)
        if create_order_form.is_valid():
            commodity = create_order_form.cleaned_data['commodity']
            pay_No = create_order_form.cleaned_data['pay_No']
            pay_No = str(user.pk) + ':' + pay_No
            pay = Pay.objects.get(pay_No=pay_No)
            try:
                commodityO = Commodity.objects.get(commodity_name=commodity)
                number = create_order_form.cleaned_data['number']
                number = int(number)
                order = Order.objects.create(commodity_id=commodityO, number=number, pay=pay)

                pay.pay_money += commodityO.commodity_price*number
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
            return render(request, 'index.html', context)
    else:
        create_order_form = createOrderForm()

    context = {}
    # context['page_title'] = '欢迎'
    context['create_order_form'] = create_order_form
    # context['commodity_list'] = commodity_list
    context['form_title'] = '##'
    return render(request, 'store/create_orders.html', context)


def creat_pay(request):
    # str
    user = request.user
    if request.method == 'POST':
        create_pay_form = createPayForm(request.POST)
        if create_pay_form.is_valid():
            shop = Shop.objects.get(shop_owner=user)
            buyer_id = create_pay_form.cleaned_data['buyer_id']
            pay_No = create_pay_form.cleaned_data['pay_No']
            pay_No = str(user.pk) + ':' + pay_No
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
            # return redirect(request.GET.get('from', reverse('home')))
            return render(request, 'index.html', context)
    else:
        create_pay_form = createPayForm()
    context = {}
    # context['page_title'] = '欢迎'
    context['create_pay_form'] = create_pay_form
    # context['commodity_list'] = commodity_list
    context['form_title'] = '##'
    return render(request, 'store/create_pay.html', context)
