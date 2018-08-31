# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 16:08:39 2018

@author: Administrator
"""

from http import cookiejar#不用自己动手来管理cookie
from urllib import request
from urllib import parse

# 创建一个cookiejar的对象
cookieJ = cookiejar.CookieJar()

# 通过HTTPCookieProcess对象来处理cookieJ
cookie_handler = request.HTTPCookieProcessor(cookieJ)

# 构建一个opener
#用一个新的可以处理cookie的Handler取代原来默认的http handler
#从而加强http handler的功能，实现其可以处理cookie
#下面就可以使用opener去发送http的请求
opener = request.build_opener(cookie_handler)
opener.addheaders=[('User-agent', "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36")]

# 准备登录
urlLogin = "http://www.renren.com/"
data = {"email":"XXX","password":"YYY"}
# post请求
data = bytes(parse.urlencode(data),encoding="utf-8")
req = request.Request(urlLogin, data=data,method="POST")
response = opener.open(req)

# 登录成功之后，去抓取首页数据
responsemyRenren = opener.open("http://www.renren.com/961482489/profile")
with open("myRenrenFromCookieJar.html", "wb") as f:
    f.write(responsemyRenren.read())









