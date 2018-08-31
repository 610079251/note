# -*- coding: utf-8 -*-
"""
Created on Fri Aug 10 09:37:38 2018

@author: Administrator
"""
import requests
import urllib
import re

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"}
#构造搜索的链接
url = "https://www.baidu.com/s?"
keyword = input("请输入您要查询的信息:")
wd = {"wd":keyword}# wd=keyword
wd = urllib.parse.urlencode(wd)#注意：这里在发起get的query之前，需要做一次urlencode
#print(wd)
fullUrl = url+wd
#print(fullUrl)

# 对搜索的链接发起一次get请求
response = requests.get(fullUrl, headers=headers)
with open("baiduSearch.html", "wb") as f:
    f.write(response.text.encode())

# 获取百度相关词的推荐
pattern = re.compile('<th><a href="([\s\S]*?)">([\s\S]*?)</a></th>')
items = re.findall(pattern, response.text)
with open("baiduSearch.txt", 'a') as f:
    for it in items:
        f.write("推荐:"+it[1]+" 链接: https://www.baidu.com"+it[0]+"\n")











