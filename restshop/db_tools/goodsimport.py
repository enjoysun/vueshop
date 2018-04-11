#!/usr/bin/env python

# encoding: utf-8

# @author: myou

# @license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.

# @contact: myoueva@gmail.com

# @software: garner

# file: goodsimport.py

# @time: 2018/4/10 22:57

import sys
import os
import django


pwd = os.path.dirname(os.path.abspath(__file__))
sys.path.append(pwd)
sys.path.append(os.path.abspath(os.path.join(pwd, '..')))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "restshop.settings")
django.setup()
from goods.models import Goods, GoodsImage, GoodCategory
from .data.product_data import Result, row_data

if __name__ == "__main__":
    print(row_data[:2])

# for goods_detail in row_data:
#     goods = Goods()
#     goods.name = goods_detail["name"]
#     goods.market_price = float(int(goods_detail["market_price"].replace("￥", "").replace("元", "")))
#     goods.shop_price = float(int(goods_detail["sale_price"].replace("￥", "").replace("元", "")))
#     goods.goods_brief = goods_detail["desc"] if goods_detail["desc"] is not None else ""
#     goods.goods_desc = goods_detail["goods_desc"] if goods_detail["goods_desc"] is not None else ""
#     goods.goods_front_image = goods_detail["images"][0] if goods_detail["images"] else ""
#
#     category_name = goods_detail["categorys"][-1]
#     category = GoodCategory.objects.filter(name=category_name)
#     if category:
#         goods.category = category[0]
#     goods.save()
#
#     for goods_image in goods_detail["images"]:
#         goods_image_instance = GoodsImage()
#         goods_image_instance.image = goods_image
#         goods_image_instance.goods = goods
#         goods_image_instance.save()