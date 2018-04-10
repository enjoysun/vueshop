from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import GoodCategory
from .serializers import Goodcateserializer

# Create your views here.


class GoodCateList(APIView):

    def get(self, request, format=None):
        goods = GoodCategory.objects.all()[:10]
        cateseralizer = Goodcateserializer(goods, many=True)
        return Response(cateseralizer.data)


