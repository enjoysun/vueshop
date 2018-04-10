#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time    : 2018/4/10 下午6:04
# @Author  : YouMing
# @Email   : myoueva@gmail.com
# @File    : serializers.py
# @Software: PyCharm
# @license : 娱网科道信息技术有限公司 copyright © 2015-2016

from rest_framework import serializers


class Goodcateserializer(serializers.Serializer):
    CATEGORY_TYPE = (
        (1, '一级类目'),
        (2, '二级类目'),
        (3, '三级类目'),
    )
    name = serializers.CharField(max_length=32, required=True)
    code = serializers.CharField(max_length=32)