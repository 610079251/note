from django.shortcuts import render
from .models import *
from django.http import HttpResponse

# Create your views here.


def parent_views(request):
    return render(request, '01_parent.html')


def child_views(request):
    return render(request, '02_child.html')


def addauthor_views(request):
    # 方式1:使用 Entry.objects.create()
    # Author.objects.create(name='朱自清',
                          # age=85,
                          # email='zhuzq@163.com')

    # 方式2:使用 Entry的save()完成增加
    # author = Author(name='老舍', age='92', email='laoshe@163.com')
    # author.save()

    # 方式3:使用字典构建对象,并调用其save()
    dic = {
        'name': '韩寒',
        'age': '35',
        'email': 'hanhan@163.com'
    }
    author = Author(**dic)
    author.save()
    return HttpResponse('Add 韩寒 OK')


def addbook_views(request):
    # 方式1
    Book.objects.create(title='背影', publicate_date='1988-12-12')
    # 方式2
    book = Book(title='三重门', publicate_date='1999-01-05')
    book.save()
    # 方式3
    dic = {
        'title': '骆驼祥子',
        'publicate_date': '1965-7-12',
    }
    book1 = Book(**dic)
    book1.save()

    return HttpResponse('Add Book OK')


def query_views(request):
    # 使用 all() 查询 Author 中的所有数据
    # authors = Author.objects.all()
    # print(authors)
    # for author in authors:
    #     print('姓名:', author.name, '年龄', author.age, '邮箱:', author.email)

    # 使用 values() 查询部分列的信息
    # authors = Author.objects.values('name', 'email')
    # print(authors)
    # for author in authors:
    #     print('姓名:' + author['name'] + ',邮箱:' + author['email'])

    # 使用　order_by() 实现排序
    # authors = Author.objects.order_by('-age', 'id')
    # print(authors)
    # for au in authors:
    #     print(au.name, au.age, au.email)

    # 使用　filter() 实现部分行的查询
    # authors = Author.objects.filter(id=1,name='韩寒')
    # print(authors)
    # for au in authors:
    #     print(au.name, au.age, au.email)

    # 使用　filter() 借助查询谓词实现部分行的查询
    # authors = Author.objects.filter(email__contains='a')
    # for au in authors:
    #     print(au.name, au.email)

    # 使用　get() 查询一条记录
    au = Author.objects.get(id__gte=1)
    print(au)
    print(au.name, au.age, au.email)

    return HttpResponse('Query OK')
