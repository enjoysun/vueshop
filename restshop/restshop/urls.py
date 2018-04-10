"""restshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.documentation import include_docs_urls
from goods.view_base import CateListView
from goods.views import GoodCateList

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    # 商品类别
    url(r'api/cate/$', GoodCateList.as_view(), name="cate.list"),

    # 文档
    url(r'doc/', include_docs_urls(title='shop')),

    # 调试接口
    url(r'^api-auth/', include('rest_framework.urls'))
]
