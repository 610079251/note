from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.


def index_views(request):
    return HttpResponse('index应用中的index视图')


def login_views(requset):
    return HttpResponse('index应用中的login视图')


def getTemp_views(request):
    # 1.通过 loader 加载模板
    t = loader.get_template('01_template.html')
    # 2.将模板对象渲染成字符串
    html = t.render()
    # 3.将字符串响应给客户端
    return HttpResponse(html)


def render_views(request):
    return render(request, '01_template.html')


def var_views(request):
    dic = {
        'title': '测试模板',
        'content': '模板的内容',
    }
    return render(request, '02_var.html', dic)


def varExer_views(request):
    title = '水浒传'
    author = '施耐庵'
    topic = '105个男人和3个女人的故事'

    # dic = {
    #     'title':title,
    #     'author':author,
    #     'topic':topic,
    # }
    # locals() 将当前函数内的局部变量封装成一个字典,效果同上
    return render(request, '03_exer.html', locals())
