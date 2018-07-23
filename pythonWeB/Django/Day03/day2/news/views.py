from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def show_views(request):
    return HttpResponse('这是news应用中的show_views视图')


def index_views(request):
    return HttpResponse('这是news应用中的index')
