# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 15:29:01 2018

@author: Administrator
"""
import urllib
import ssl

url = "https://www.12306.cn/mormhweb/"
ua_headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"}

context = ssl._create_unverified_context()# 创建一个不需要认证的SSL上下文

# HTTP request
req = urllib.request.Request(url, headers=ua_headers)
# HTTP response
# If *context* is specified, it must be a ssl.SSLContext instance describing
#the various SSL options. See HTTPSConnection for more details.
response = urllib.request.urlopen(req,context=context) #CertificateError

with open("12306.html", "wb") as f:
    f.write(response.read())




