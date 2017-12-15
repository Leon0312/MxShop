from datetime import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class UserProfile(AbstractUser):
    """
    用户信息
    """
    gender_choice={
    }
    name = models.CharField(max_length=30, null=True, blank=True, verbose_name="姓名")
    birthday = models.DateField(null=True, blank=True, verbose_name="出生日期")
    mobile = models.CharField(max_length=11, verbose_name="手机号码")
    gender = models.CharField(max_length=6, choices=(("male", u"男"), ("female", u"女")), verbose_name="性别")
    email = models.CharField(max_length=100, null=True, blank=True, verbose_name="邮箱")

    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = "用户信息"

    def __repr__(self):
        return self.username


class VerifyCode(models.Model):
    """
    短信验证码
    """
    code = models.CharField(max_length=10, verbose_name="验证码")
    mobile = models.CharField(max_length=30, verbose_name="手机号码")
    # 这里使用datetime.now 而不能使用.now（） 方法，因为后者获取的时间是程序编译的时间。
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "验证码"
        verbose_name_plural = "验证码"
    # repr方法用于返回对象字符串表达式，或者选取一个字段返回

    def __repr__(self):
        return self.code
