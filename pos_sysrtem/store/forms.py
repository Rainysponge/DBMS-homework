from django import forms
from django.contrib import auth
from django.contrib.auth.models import User
from .models import Order, Pay, CommodityToshop, Commodity


class createOrderForm(forms.Form):
    pay_No = forms.CharField(label='账单编号',
                             max_length=16, min_length=1,
                             widget=forms.TextInput(attrs={'class': 'form-control'}))
    commodity = forms.CharField(label='商品',
                                max_length=30, min_length=2,
                                widget=forms.TextInput(attrs={'class': 'form-control'}))
    number = forms.CharField(label='数量',
                             max_length=30, min_length=1,
                             widget=forms.TextInput(attrs={'class': 'form-control'}))

    # widget=forms.TextInput(attrs={'class': 'form-control'}))


class createPayForm(forms.Form):
    pay_No = forms.CharField(label='账单编号',
                             max_length=16, min_length=1,
                             widget=forms.TextInput(attrs={'class': 'form-control'}))
    buyer_id = forms.CharField(label='学号/工号',
                               max_length=30, min_length=2,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))


class createCommodity(forms.Form):
    # commodity_price = models.IntegerField(default=1)
    # commodity_name = models.CharField(max_length=10)
    # commodity_contends = models.TextField()
    commodity_name = forms.CharField(label='商品名称',
                                     max_length=10, min_length=1,
                                     widget=forms.TextInput(attrs={'class': 'form-control'}))
    number = forms.CharField(label='数量',
                             max_length=30, min_length=1,
                             widget=forms.TextInput(attrs={'class': 'form-control'}))
