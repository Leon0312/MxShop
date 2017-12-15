__author__ = 'Leon'
# -*- coding:utf-8 -*-

from rest_framework import serializers
from goods.models import Goods


class GoodsSerializer(serializers.Serializer):
    """
    Serializer for the Goods
    """
    name = serializers.CharField(required=True, max_length=100)
    click_num = serializers.IntegerField(default=0)
    add_time = serializers.DateTimeField()
    front_page_image = serializers.ImageField()

    def create(self, validated_data):
        """
        创建并返回一个good 实例
        :param validated_data:
        :return:
        """
        return Goods.objects.create(**validated_data)
