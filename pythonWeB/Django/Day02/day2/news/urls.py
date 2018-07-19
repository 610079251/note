from django.conf.urls import url
from .views import *

# 只有请求路径是 http://localhost:8000/news/...
# 才能进入到此路由配置
urlpatterns = [
    # 请求路径是 show 的时候,则交给show_views去处理
    url(r'^show/$', show_views),
    # 请求路径是 index 的时候,则交给index_views去处理
    url(r'^$', index_views),
]
