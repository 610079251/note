# -*- coding: utf-8 -*-
"""
Created on Thu Aug  9 09:50:30 2018

@author: Administrator
"""

import re

strs = "hello_Python3_world!"

p1 = '.*_'#贪婪模式
p2 = '.*?_'#懒惰模式
pattern1 = re.compile(p1)
pattern2 = re.compile(p2)
print(re.findall(pattern1, strs))#贪婪的结果
print(re.findall(pattern2, strs))#精细的全部结果





