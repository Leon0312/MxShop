# coding:utf-8
__author__ = 'Leon'
__date__ = '2017/12/1 9:59'

from django.views.generic.base import View
from goods.models import Goods


class GoodsListView(View):
    """
    通过 ListView实现商品列表页
    """
    def get(self, request):

        json_list = []
        # 这里的[y:x]  x 代表的的取对象的个数从默认第一条开始取到第十条数据。y代表从第几条开始取。
        goods = Goods.objects.all()[:10]
        # for good in goods:
        #     json_dict = {}
        #     json_dict['name'] = good.name
        #     json_dict['category'] = good.category.name
        #     json_dict['market_price'] = good.market_price
        #     add_time = str(good.add_time)
        #     json_dict['add_time'] = add_time
        #     json_list.append(json_dict)
        # from django.forms.models import model_to_dict
        # for good in goods:
        #     json_dict = model_to_dict(good)
        #     json_list.append(json_dict)
        from django.core import serializers
        from django.http.response import JsonResponse
        json_data = serializers.serialize('json', goods)
        # json_data = json.loads(json_data)
        return JsonResponse(json_data, safe=False)
