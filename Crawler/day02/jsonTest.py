# -*- coding: utf-8 -*-
"""
Created on Wed Aug  8 16:19:09 2018

@author: Administrator
"""

import json

jsonDict = {'One':'1', 'Two':'2'}

# dict -> json str
jsonDumps = json.dumps(jsonDict)#json encode
print(type(jsonDumps))
print(jsonDumps)

# json str -> dict
jsonLoads = json.loads(jsonDumps)# json decode
print(type(jsonLoads))
for key,value in jsonLoads.items():
    print(key,value)





