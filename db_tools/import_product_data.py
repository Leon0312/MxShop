# coding:utf-8
__author__ = 'Leon'
__date__ = '2017/11/30 11:19'

import os
import sys

#  独立的使用Models

pwd = os.path.dirname(os.path.realpath(__file__))
sys.path.append(pwd+"../")
# 以下确保能正确的调用项目中模块内容
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "MxShop.settings")

import django
django.setup()

from goods.models import Goods, GoodsCategory, GoodsImage
from db_tools.data.product_data import row_data

for goods_data in row_data:
    goods = Goods()
    goods.name = goods_data["name"]
    goods.market_price = float(goods_data["market_price"].replace("￥", "").replace("元", ""))
    goods.shop_price = float(goods_data["sale_price"].replace("￥", "").replace("元", ""))
    goods.goods_brief = goods_data["desc"] if goods_data["desc"] is not None else ""
    goods.goods_desc = goods_data["goods_desc"] if goods_data["goods_desc"] is not None else ""
    # 这里只取第一张
    goods.front_page_image = goods_data["images"][0] if goods_data["images"] else ""

    category_name = goods_data["categorys"][-1]
    category = GoodsCategory.objects.filter(name=category_name)
    if category:
        goods.category = category[0]
    goods.save()
    for goods_image in goods_data["images"]:
        goods_image_instance = GoodsImage()
        goods_image_instance.image_url = goods_image
        goods_image_instance.goods = goods
        goods_image_instance.save()
