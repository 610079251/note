from django.shortcuts import render

# Create your views here.


def parent_views(request):
    return render(request, '01_parent.html')


def child_views(request):
    return render(request, '02_child.html')
