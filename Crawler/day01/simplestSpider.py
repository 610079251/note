# -*- coding: utf-8 -*-
"""
Created on Tue Aug  7 11:13:35 2018

@author: Administrator
"""
from urllib import request
# urllib.request
# 我们知道HTTP协议需要Request请求，
#服务器返回Response的响应

# HTTP Request:
# 这里request.Request("http://www.sina.com.cn") 构造出一个对象
#准备对新浪的服务器发起请求
# request.urlopen 对新浪的服务器发起请求
# request.urlopen返回的是http.client.HTTPResponse对象；

print(request.urlopen("http://www.sina.com.cn"
                      ).getcode()) #200 OK
print(request.urlopen("http://www.sina.com.cn"
                      ).read().decode())




# info函数的实现
#递归








