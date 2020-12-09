from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('shop_list/', views.shop_list, name='shop_list'),
    path('myShopList/', views.myshopList, name='myShopList'),

    path('create_pay/<int:shop_pk>', views.creat_pay, name='create_pay'),
    path('create_shop/', views.create_shop, name='create_shop'),
    path('update_commodity/', views.update_commodity, name='update_commodity'),
    path('create_orders/<int:shop_pk>', views.create_orders, name='create_orders'),
]

