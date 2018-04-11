from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
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


class GoodsimagePagenation(PageNumberPagination):
    page_size = 10
    max_page_size = 20
    page_query_param = 'page'
    page_size_query_param = 'page_size'
    


class Goodsimagelist(mixins.ListModelMixin, generics.GenericAPIView):
    # def get(self, request, format=None):
    #     images = GoodsImage.objects.all()
    #     imgseralizer = Goodimageseralizer(images, many=True)
    #     return Response(imgseralizer.data)
    queryset = GoodsImage.objects.all()
    serializer_class = Goodimageseralizer
    pagination_class = GoodsimagePagenation
    def get(self, request):
        return self.list(request)


