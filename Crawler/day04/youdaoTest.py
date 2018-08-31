# -*- coding: utf-8 -*-
"""
Created on Fri Aug 10 11:11:59 2018

@author: Administrator
"""
from urllib import parse,request
import re
import requests
import json

def getTInfo(key):   
    # 通过抓包的方式获取的url，并不是浏览器上显示的url
    url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=null"

    # 完整的headers
    headers = {
            "Accept" : "application/json, text/javascript, */*; q=0.01",
            "X-Requested-With" : "XMLHttpRequest",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0",
            "Content-Type" : "application/x-www-form-urlencoded; charset=UTF-8",
        }
    
    formdata = {
    "i":key,
    "from":"auto",
    "to":"auto",
    "smartresult":"dict",
    "client":"fanyideskweb",
    "salt":"1511219405946",
    "sign":"f8965f67a1d3eee8a69ddf8ccc5f582b",
    "doctype":"json",
    "version":"2.1",
    "keyfrom":"fanyi.web",
    "action":"FY_BY_REALTIME",
    "typoResult":"false"
    }
    
    # 由于urllib在做post时需要data是bytes，所以这里需要对
    #formdata做一次类型的处理，转成bytes
    # data=parse.urlencode(formdata).encode("utf-8")
    data=bytes(parse.urlencode(formdata),encoding='utf-8')
    #  做一次urlencode
    #利用Request将headers，dict，data整合成一个对象传入urlopen
#    req = request.Request(url,data,headers,method='POST')
#    response=request.urlopen(req)
#    info = response.read().decode('utf-8')
    #print(info)
    req = requests.post(url, headers=headers, data=data)
    info = req.text
    #print(req.text)
    
    
    #使用正则表达式取出翻译之后的信息
#    strRule = re.compile('"tgt":"(.*?)"}')
#    info2 = strRule.findall(info)
#    for i in info2:
#               i = i.replace('"',"")
#    return info2[0]
    
    # 使用json来提取翻译的信息
    jsonloads = json.loads(info) # json encode 
    return jsonloads["translateResult"][0][0]["tgt"]

#print(getTInfo("hello"))
if __name__ == "__main__":
    info = input("请输入您要查询的单词：")
    print(getTInfo(info))
