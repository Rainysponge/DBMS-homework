from django.db import models


# Create your models here.
class Shop(models.Model):
    shop_name = models.CharField(max_length=32, null=True)
    shop_owner = models.CharField(max_length=32, null=True)
    shop_ownerID = models.CharField(max_length=18)
    shop_position = models.CharField(max_length=32, null=True)
    phone_number = models.CharField(max_length=11, null=True)
    contends = models.TextField()
    create_time = models.DateTimeField()
    last_update = models.DateTimeField()
    is_active = models.BooleanField()


class PosInfo(models.Model):
    shop_id = models.ForeignKey(Shop, on_delete=models.CASCADE)
    is_active = models.BooleanField()
    start_time = models.DateTimeField()



class CommodityToshop(models.Model):
    shop_id = models.CharField(max_length=8)
    commodity_id = models.CharField(max_length=16)


class Pay(models.Model):
    buyer_id = models.CharField(max_length=10)
    pay_time = models.CharField(max_length=10)
    pay_money = models.CharField(max_length=10)
    order_id = models.CharField(max_length=10)


class Commodity(models.Model):
    commodity_id = models.CharField(max_length=10)
    commodity_price = models.CharField(max_length=10)
    commodity_name = models.CharField(max_length=10)
    commodity_contends = models.TextField()


class Order(models.Model):
    order_id = models.CharField(max_length=10)
    commodity_id = models.CharField(max_length=10)
