from django.contrib import admin
from .models import Shop, PosInfo, Pay, Commodity, CommodityToshop, Order


# Register your models here.

@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = ('shop_id', 'shop_name', 'shop_owner')


@admin.register(PosInfo)
class PosInfoAdmin(admin.ModelAdmin):
    list_display = ('shop_id', 'is_active')


@admin.register(Pay)
class PayAdmin(admin.ModelAdmin):
    list_display = ('id', 'shop', 'pay_No', 'buyer_id', 'pay_time')


@admin.register(Commodity)
class CommodityAdmin(admin.ModelAdmin):
    list_display = ('id', 'shop', 'commodity_name')


@admin.register(CommodityToshop)
class CommodityToshop(admin.ModelAdmin):
    list_display = ('shop_owner', 'commodity_id')


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ( 'pay', 'commodity_id')
