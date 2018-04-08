#!/usr/bin/env python

# encoding: utf-8

# @author: myou

# @license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.

# @contact: myoueva@gmail.com

# @software: garner

# file: view_base.py

# @time: 2018/4/8 23:31

from django.views.generic.base import View
from goods.models import GoodCategory
from django.http import HttpResponse
import json


class CateListView(View):

    def get(self, request):

        cate_list = []
        goods = GoodCategory.objects.all()[:10]
        for good in goods:
            cate = {}
            cate["name"] = good.name
            cate["code"] = good.code
            cate["desc"] = good.descripition
            cate["type"] = good.category_type
            cate["fid"] = good.fid
            cate["istab"] = good.is_tab
            cate_list.append(cate)
        result = json.dumps(cate_list)
        return HttpResponse(result, content_type="application/json")

