from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('shop_list/', views.shop_list, name='shop_list'),
    path('myShopList/', views.myshopList, name='myShopList'),
    path('shop_info/<int:shop_pk>', views.shop_info, name='shop_info'),
    path('create_pay/<int:shop_pk>', views.creat_pay, name='create_pay'),
    path('create_shop/', views.create_shop, name='create_shop'),
    path('create_commodity/<int:shop_pk>', views.create_commodity, name='create_commodity'),
    path('update_commodity_price/<int:shop_pk>', views.update_commodity_price, name='update_commodity_price'),
    path('create_orders/<int:shop_pk>', views.create_orders, name='create_orders'),
    path('orders_in_pay/<int:pay_pk>', views.orders_in_pay, name='orders_in_pay'),
    path('shop_info_with_charts/<int:shop_pk>', views.shop_info_with_charts, name='shop_info_with_charts'),
]

