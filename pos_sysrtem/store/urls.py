from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('shop_list/', views.shop_list, name='shop_list'),
    path('create_orders/', views.create_orders, name='create_orders'),
    path('create_pay/', views.creat_pay, name='create_pay'),
]

