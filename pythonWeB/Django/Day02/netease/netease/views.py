from django.http import HttpResponse


def first_views(request):
    return HttpResponse('我的第一个django程序')


def run_arg1_views(request, num1):
    return HttpResponse("参数为:" + num1)

# num1 对应的是地址中的 四位数字
# num2 对应的是地址中的 两位数字


def run_arg2_views(request, num1, num2):
    return HttpResponse("参数1:" + num1 + ",参数2:" + num2)


def show_views(request, name, age):
    return HttpResponse("姓名:<h1>" + name + "</h1>,年龄:<h1>" + age + "</h1>")
