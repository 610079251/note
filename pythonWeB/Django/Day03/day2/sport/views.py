from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index_views(request):
    return HttpResponse('sport应用中的index')


def params_views(request):
    return render(request, '01_params.html')


def name_views(request):
    return HttpResponse('已经成功到达02_name')


def name_arg_views(request, num):
    return HttpResponse('传递的参数为:' + num)
