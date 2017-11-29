from django.db import models
from datetime import datetime

from DjangoUeditor.models import UEditorField
# Create your models here.


class GoodsCategory(models.Model):
    """
    商品类别
    """
    CATEGORY_TYPE = (
        ("1", u"一级类目"),
        ("2", u"二级类目"),
        ("3", u"三级类目"),
    )
    name = models.CharField(default="", max_length=30, verbose_name="类别名", help_text="类别名")
    code = models.CharField(default="", max_length=30, verbose_name="类别code", help_text="类别code")
    # 类的简单描述
    desc = models.TextField(default="", verbose_name="类目描述", help_text="类目描述")
    # category_type 用于说明该类的级别（比如三层级目录，）
    category_type = models.CharField(choices=CATEGORY_TYPE, max_length=10, verbose_name="类目级别", help_text="类目级别")
    parent_category = models.ForeignKey("self", null=True, blank=True, related_name="sub_cat", verbose_name="父类别")

    is_tab = models.BooleanField(default=False, verbose_name="是否导航", help_text="是否导航")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "商品类别"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class GoodsCategoryBrand(models.Model):
    """
    品牌名
    """
    name = models.CharField(default="", max_length=30, verbose_name="品牌名", help_text="品牌名")
    desc = models.CharField(default="", max_length=30, verbose_name="品牌描述", help_text="品牌描述")
    # 用于存储图片文件。
    image = models.ImageField(max_length=200, upload_to="brand/images")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "品牌名"
        verbose_name_plural = verbose_name
    # 返回对object的描述

    def __str__(self):
        return self.name


class Goods(models.Model):
    """
    商品
    """
    category = models.ForeignKey(GoodsCategory, null=True, blank=True, verbose_name="目录")
    goods_sn = models.CharField(default="", max_length=50, verbose_name="商品货号", help_text="商品货号")
    name = models.CharField(max_length=100, verbose_name="商品名字")
    click_num = models.IntegerField(default=0, verbose_name="点击数")
    sold_num = models.IntegerField(default=0, verbose_name="销量")
    goods_num = models.IntegerField(default=0, verbose_name="库存")
    market_price = models.FloatField(default=0, verbose_name="市场价格")
    shop_price = models.FloatField(default=0, verbose_name="市场价")
    # 商品描述
    goods_brief = models.TextField(max_length=500, verbose_name="简述商品")
    # 富文本描述
    goods_desc = UEditorField(verbose_name=u"内容", imagePath="goods/images/", width=1000, height=300,
                              filePath="goods/files/", default="")
    ship_free = models.BooleanField(default=False, verbose_name="是否包邮")
    front_page_image = models.ImageField(upload_to="", verbose_name="单独的封面图，不从轮播图中取")
    is_new = models.BooleanField(default=False, verbose_name="是否为新品")
    is_hot = models.BooleanField(default=False, verbose_name="是否热销")

    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "商品"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class GoodsImage(models.Model):
    """
    商品轮播图
    """
    goods = models.ForeignKey(Goods, verbose_name="商品", related_name="images")
    image = models.ImageField(upload_to="goods/images/", verbose_name="详情")
    image_url = models.CharField(max_length=300, null=True, blank=True, verbose_name="图片Url")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "商品图片"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.goods.name


class Banner(models.Model):
    goods = models.ForeignKey(Goods, verbose_name="商品")
    image = models.ImageField(upload_to="banner", verbose_name="轮播图片（首页）")
    index = models.IntegerField(default=0, verbose_name="轮播顺序")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "轮播图"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.goods.name
