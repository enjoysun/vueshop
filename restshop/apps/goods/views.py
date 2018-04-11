from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import GoodCategory, GoodsImage
from .serializers import Goodcateserializer, Goodimageseralizer

# Create your views here.


class GoodCateList(APIView):

    def get(self, request, format=None):
        goods = GoodCategory.objects.all()[:10]
        cateseralizer = Goodcateserializer(goods, many=True)
        return Response(cateseralizer.data)


class GoodsList(APIView):
    def get(self, request, format=None):
        pass


class Goodsimagelist(APIView):
    def get(self, request, format=None):
        images = GoodsImage.objects.all()
        imgseralizer = Goodimageseralizer(images, many=True)
        return Response(imgseralizer.data)


