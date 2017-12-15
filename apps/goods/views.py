from django.shortcuts import render
from .models import Goods
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from goods.serializers import GoodsSerializer
# Create your views here.


class GoodsListView(APIView):
    """
    List all goods, or create a new good
    """
    def get(self, request, format=None):
        goods = Goods.objects.all()[:10]
        goods_serializer = GoodsSerializer(goods, many=True)
        return Response(goods_serializer.data)

    def post(self, request, format=None):
        serializer = GoodsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(request.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
