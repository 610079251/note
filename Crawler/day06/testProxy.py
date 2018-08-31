# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 15:39:35 2018

@author: Administrator
"""
from urllib import request
import re

# 检验代理服务器,怎么知道当前和Internet连通的
def check_proxy(html):
    pattern = re.compile("<title>百度一下，你就知道</title>")
    title = re.findall(pattern, html)
    if title is None:
        return False
    else:
        return True


# 设置代理服务器
def use_http_proxy(proxy_addr):
    # 这里需要使用代理服务器的Handler
    proxyH = request.ProxyHandler({"http":proxy_addr})
    
    # 由这个proxy handler创建一个HTTP的opener
    opener = request.build_opener(proxyH)
    
    # 把这个opener装载到urllib中，以备使用
    request.install_opener(opener)
    
    # 发起HTTP请求
    try:
        response = request.urlopen("http://www.baidu.com")
        # 读取信息，判断此代理是否可用
        html = response.read().decode("utf-8")
    except:
        return False
    return check_proxy(html)
    
if __name__ == "__main__": 
    proxy_addr = "116.62.23.142:16816"
    print(use_http_proxy(proxy_addr))
