from django.db import models
from datetime import datetime

from django.contrib.auth import get_user_model
from goods.models import Goods
User = get_user_model()
# Create your models here.


class ShoppingCart(models.Model):
    """
    购物车
    """
    user = models.ForeignKey(User, verbose_name="")
    goods = models.ForeignKey(Goods)
    goods_num = models.IntegerField(default=0, verbose_name="加购商品数量")

    add_time = models.DateTimeField(default=datetime, verbose_name="添加时间")

    class Meta:
        verbose_name = "购物车"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "%s(%d)".format(self.goods.name, self.goods_num)


class OrderInfo(models.Model):
    """
    订单信息
    """
    ORDER_STATUS = (
        ("success", "成功"),
        ("cancel", "取消"),
        ("to pay", "待支付")
    )
    # PAY_TYPE = (
    #     ("wechat", "微信支付"),
    #     ("alipay", "支付宝"),
    # )
    user = models.ForeignKey(User, verbose_name="用户")
    order_sn = models.CharField(max_length=30, unique=True, verbose_name="订单编号")
    trade_no = models.CharField(max_length=100, unique=True, null=True, blank=True, verbose_name="第三方支付产生的订单编号")
    pay_status = models.CharField(choices=ORDER_STATUS, max_length=10, verbose_name="订单支付状态")
    post_script = models.CharField(max_length=200, verbose_name="订单留言/备注")
    order_mount = models.FloatField(default=0.0, verbose_name="订单金额")
    pay_time = models.DateTimeField(null=True, blank=True,verbose_name="支付时间")

    # 用户相关信息
    address = models.CharField(max_length=100, default="", verbose_name="收货地址")
    signer_name = models.CharField(max_length=20, default="", verbose_name="收件人")
    signer_mobile = models.CharField(max_length=11, verbose_name="联系电话")

    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "订单信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.order.order_sn)


class OrderGoods(models.Model):
    """
    订单中商品详情
    """
    order = models.ForeignKey(OrderInfo)
    goods = models.ForeignKey(Goods)
    goods_num = models.IntegerField(default=0, verbose_name="商品数量")

    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "订单中商品详情"
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.order.order_sn)

