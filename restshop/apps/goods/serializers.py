#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time    : 2018/4/10 下午6:04
# @Author  : YouMing
# @Email   : myoueva@gmail.com
# @File    : serializers.py
# @Software: PyCharm
# @license : 娱网科道信息技术有限公司 copyright © 2015-2016

from rest_framework import serializers
<<<<<<< HEAD
from .models import Goods, GoodCategory
=======
from .models import Goods, GoodCategory, GoodsImage
>>>>>>> 4a67a8de468a7a704ac13ba8c64e3f1298e438b1


class Goodcateserializer(serializers.ModelSerializer):
    # CATEGORY_TYPE = (
    #     (1, '一级类目'),
    #     (2, '二级类目'),
    #     (3, '三级类目'),
    # )
    # name = serializers.CharField(max_length=32, required=True)
    # code = serializers.CharField(max_length=32)
    class Meta:
        model = GoodCategory()
        fields = '__all__'
        # fields = ['category', 'name']

    def create(self, validated_data):
        return Goods.objects.create(validated_data)


class Goodsseralizer(serializers.ModelSerializer):
    class Meta:
        model = Goods()
        fields = '__all__'


class Goodimageseralizer(serializers.ModelSerializer):
    goods = Goodsseralizer()
    class Meta:
        model = GoodsImage()
        fields = '__all__'