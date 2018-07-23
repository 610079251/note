from django.shortcuts import render

# Create your views here.


def login_views(request):
    return render(request, '01_login.html')
