from django.conf.urls import url
from .views import *

# 请求地址 http://localhost:8000/sprot/...
# 请求会转发到此处

urlpatterns = [
    url(r'^index/$', index_views),
]
