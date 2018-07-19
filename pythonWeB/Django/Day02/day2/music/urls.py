from django.conf.urls import url
from .views import *

# 请求路径是 http://localhost:8000/music/的时候
# 请求才会到此
urlpatterns = [
    url(r'^index/$', index_views),
]
