"""day2 URL Configuration

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
from django.conf.urls import url, include
from django.contrib import admin
# 主路由配置文件
urlpatterns = [
    # 请求路径 http://localhost:8000/...
    # 一律都交给index应用中的urls模块去处理
    url(r'^', include('index.urls')),
    url(r'^admin/', admin.site.urls),
    # 请求路径 http://localhost:8000/news/...
    # 一律都交给news应用中的urls模块去处理
    url(r'^news/', include('news.urls')),
    # 请求路径 http://localhost:8000/music/...
    # 一律都交给music应用中的urls模块去处理
    url(r'^music/', include('music.urls')),
    # 请求路径 http://localhost:8000/sport/...
    # 一律都交给sport应用中的urls模块去处理
    url(r'^sport/', include('sport.urls')),

]