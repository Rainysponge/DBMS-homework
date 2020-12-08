from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.
class Shop(models.Model):
    shop_name = models.CharField(max_length=32, null=True)
    shop_owner = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    # shop_ownerID = models.CharField(max_length=18)
    shop_position = models.CharField(max_length=32, null=True)
    phone_number = models.CharField(max_length=11, null=True)
    contends = models.TextField()
    create_time = models.DateTimeField()
    last_update = models.DateTimeField()
    is_active = models.BooleanField()


class PosInfo(models.Model):
    shop_id = models.ForeignKey(Shop, on_delete=models.CASCADE, null=True)

    is_active = models.BooleanField()
    start_time = models.DateTimeField()


class Commodity(models.Model):
    # commodity_id = models.CharField(max_length=10)
    shop = models.ForeignKey(Shop, on_delete=models.DO_NOTHING, null=True)
    commodity_price = models.IntegerField(default=1)
    commodity_name = models.CharField(max_length=10)
    commodity_contends = models.TextField()

    def __str__(self):
        return self.commodity_name


class CommodityToshop(models.Model):
    shop_owner = models.ForeignKey(Shop, on_delete=models.CASCADE, null=True)
    commodity_id = models.ForeignKey(Commodity, on_delete=models.CASCADE)


class Pay(models.Model):
    pay_No = models.CharField(max_length=24, null=True)
    shop = models.ForeignKey(Shop, on_delete=models.DO_NOTHING, null=True)
    POS = models.ForeignKey(PosInfo, on_delete=models.DO_NOTHING, null=True)
    buyer_id = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    pay_time = models.DateTimeField(default=timezone.now)
    pay_money = models.IntegerField(default=0)


#     先一次只能购买一次商品
class Order(models.Model):
    # order_id = models.CharField(max_length=10, null=True)
    commodity_id = models.ForeignKey(Commodity, on_delete=models.DO_NOTHING)
    number = models.IntegerField(default=0)
    pay = models.ForeignKey(Pay, on_delete=models.DO_NOTHING, null=True)
