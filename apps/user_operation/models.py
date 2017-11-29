from django.db import models
from django.contrib.auth import get_user_model
from goods.models import Goods
from datetime import datetime

User = get_user_model()
# Create your models here.

"""
    用户操作，包括收藏，留言
 """


class UserFav(models.Model):
    """
    收藏
    """
    user = models.ForeignKey(User, verbose_name="用户")
    goods = models.ForeignKey(Goods, verbose_name="商品")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "用户收藏"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.user.name


class UserLeavingMessage(models.Model):
    """
    留言信息
    """
    MSG_CHOICES = (
        (1, "留言"),
        (2, "询问"),
        (3, "投诉"),
        (4, "售后"),
        (5, "求购")
    )
    user = models.ForeignKey(User, verbose_name="用户")
    message_type = models.CharField(default=1, max_length=5, choices=MSG_CHOICES, verbose_name="留言类型")
    subject = models.CharField(max_length=30, default=" ", verbose_name="留言标题")
    message = models.TextField(default=" ", verbose_name="留言内容", help_text="留言内容")
    file = models.FileField(upload_to="")

    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "留言信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.subject


class UserAddress(models.Model):
    """
    收货地址
    """
    user = models.ForeignKey(User, verbose_name="用户")
    district = models.CharField(default="", max_length=100, verbose_name="配送区域")
    address = models.CharField(default="", max_length=100, verbose_name="详细地址")
    signer_name = models.CharField(default="", max_length=30, verbose_name="收货人姓名")
    signer_mobile = models.CharField(default="",max_length=11, verbose_name="收货人电话")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "收货地址"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.address

