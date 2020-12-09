from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.
class Shop(models.Model):
    shop_id = models.CharField(max_length=12, null=True)  # 商店编号————为一个用户开多个店铺做准备
    shop_name = models.CharField(max_length=32, null=True)
    shop_owner = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    # shop_ownerID = models.CharField(max_length=18)
    shop_position = models.CharField(max_length=32, null=True)
    phone_number = models.CharField(max_length=11, null=True)
    contends = models.TextField(null=True)
    create_time = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)


class PosInfo(models.Model):
    shop_id = models.ForeignKey(Shop, on_delete=models.CASCADE, null=True)  # 这个就是商店的外键，只是没改名字而已

    is_active = models.BooleanField()
    start_time = models.DateTimeField()


class Commodity(models.Model):
    # commodity_id = models.CharField(max_length=10)
    shop = models.ForeignKey(Shop, on_delete=models.DO_NOTHING, null=True)
    commodity_price = models.IntegerField(default=1)
    commodity_name = models.CharField(max_length=10)
    commodity_contends = models.TextField(null=True)

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
    # 通过相同的pay_No把order整合成账单，先建立账单，然后在添加order buyer_id就是买家的外键，没改名而已


class Order(models.Model):
    # order_id = models.CharField(max_length=10, null=True)
    commodity_id = models.ForeignKey(Commodity, on_delete=models.DO_NOTHING)
    number = models.IntegerField(default=0)
    pay = models.ForeignKey(Pay, on_delete=models.DO_NOTHING, null=True)
    # 一个订单一件商品
