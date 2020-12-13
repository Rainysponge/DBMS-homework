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


class createShopForm(forms.Form):
    shop_id = forms.CharField(label='商店编号',
                              max_length=10, min_length=1,
                              widget=forms.TextInput(attrs={'class': 'form-control'}))
    shop_name = forms.CharField(label='商店名称',
                                max_length=10, min_length=1,
                                widget=forms.TextInput(attrs={'class': 'form-control'}))
    phone_number = forms.CharField(label='联系电话',
                                   max_length=11, min_length=2,
                                   widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '请输入可用的电话号码'}))


class createCommodityForm(forms.Form):
    # commodity_price = models.IntegerField(default=1)
    # commodity_name = models.CharField(max_length=10)
    # commodity_contends = models.TextField()
    # shop_id = forms.CharField(label='商店编号',
    #                           max_length=10, min_length=1,
    #                           widget=forms.TextInput(attrs={'class': 'form-control'}))
    commodity_name = forms.CharField(label='商品名称',
                                     max_length=10, min_length=1,
                                     widget=forms.TextInput(attrs={'class': 'form-control'}))
    commodity_price = forms.CharField(label='商品价格',
                                      max_length=10, min_length=1,
                                      widget=forms.TextInput(attrs={'class': 'form-control'}))


class updateCommodityForm(forms.Form):
    commodity_name = forms.CharField(label='商品名称',
                                     max_length=10, min_length=1,
                                     widget=forms.TextInput(attrs={'class': 'form-control',
                                                                   'placeholder': '请输入已有的商品名称'}))

    commodity_price = forms.CharField(label='商品价格',
                                      max_length=10, min_length=1,
                                      widget=forms.TextInput(attrs={'class': 'form-control',
                                                                    'placeholder': '请输入想要更改的价格'}))


class updateShopInfoForm(forms.Form):
    # shop_position = models.CharField(max_length=32, null=True)
    # contends = models.TextField(null=True)
    shop_position = forms.CharField(label='商店位置',
                                    max_length=12, min_length=1,
                                    widget=forms.TextInput(attrs={'class': 'form-control',
                                                                  'placeholder': '请输入真实的地址信息'}))
    contends = forms.CharField(label='简介',
                               max_length=30, min_length=1,
                               widget=forms.TextInput(attrs={'class': 'form-control',
                                                             'placeholder': '请输入真实的地址信息'}))
