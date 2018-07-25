from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^01_parent/$', parent_views),
    url(r'^02_child/$', child_views),
    url(r'^03_addauthor/$', addauthor_views),
    url(r'^04_addbook/$', addbook_views),
    url(r'^05_query/$', query_views),
]
