# -*- coding: utf-8 -*-
"""
Created on Wed Aug  8 10:03:08 2018

@author: Administrator
"""

#User-Agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36

#from urllib import request
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36"}
#url = "http://www.sina.com.cn"
#req = request.Request(url, headers=headers)
#print(request.urlopen(req).read().decode("utf-8"))

import requests
response = requests.get("http://www.sina.com.cn",
                        headers=headers)
response.encoding = "utf-8"
#print(response.status_code)
with open("sina.html", "wb") as f:
    f.write(response.text.encode("utf-8"))
#print(response.text)











