"""netease URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from .views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # 自定义url函数:定义一个访问路径,映射到对应的视图中

    # 访问路径 http://localhost:8000/first/,
    # 则由first_views视图处理
    url(r'^first/$', first_views),

    # 访问路径 http://localhost:8000/run/两位数字/
    # 交给 run_arg1_views 处理
    url(r'^run/(\d{2})/$', run_arg1_views),

    # 访问路径 http://localhost:8000/run/四位数字/两位数字
    # 交给 run_arg2_views 处理
    url(r'^run/(\d{4})/(\d{2})/$', run_arg2_views),

    # 访问路径 http://localhost:8000/show/
    # 交给 show_views 处理
    url(r'^show/$', show_views, {'name': 'zsf', 'age': '25'})
]
