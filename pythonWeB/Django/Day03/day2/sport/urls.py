from django.conf.urls import url
from .views import *

# 请求地址 http://localhost:8000/sprot/...
# 请求会转发到此处

urlpatterns = [
    url(r'^index/$', index_views),
    url(r'^01_params/$', params_views),
    url(r'^02_name/$', name_views, name='page2'),
    url(r'^03_name/(\d{4})', name_arg_views, name='page3')
]
