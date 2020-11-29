from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('shop_list/', views.shop_list, name='shop_list'),
]

