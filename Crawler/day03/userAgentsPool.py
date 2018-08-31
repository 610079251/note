# -*- coding: utf-8 -*-
"""
Created on Thu Aug  9 09:15:05 2018

@author: Administrator
"""

import requests
import random
user_agentList = ["Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)",
                  "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)",
                  "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)",
                  "Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
                  "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)"
                  ]

for _ in range(10):
    headers = {"User-Agent":random.choice(user_agentList)}
    print(headers)
    response = requests.get("http://www.sina.com.cn", headers=headers)
    response.encoding = "utf-8"
    print(response.status_code)
    
    
    
    
    
    
    