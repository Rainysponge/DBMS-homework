from django import forms
from django.contrib import auth
from django.contrib.auth.models import User
from .models import Order, Pay, CommodityToshop, Commodity


class createOrderForm(forms.Form):
    COMMODITY = []
    for item in Commodity.objects.all():
        COMMODITY.append([item, item.commodity_name])
    commodity = forms.ChoiceField(label='商品', choices=COMMODITY)
    number = forms.CharField(label='数量',
                             max_length=30, min_length=1,
                             widget=forms.TextInput(attrs={'class': 'form-control'}))

    # pay = forms.CharField(label='订单编号',
    #                       max_length=30, min_length=1,
    #                       widget=forms.TextInput(attrs={'class': 'form-control'}))
