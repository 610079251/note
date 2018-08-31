# -*- coding: utf-8 -*-
"""
Created on Wed Aug  8 17:49:08 2018

@author: Administrator
"""

from bs4 import BeautifulSoup

doc = ['<html><head><title>Page title</title></head>',
       '<body><p id="firstpara" align="center">This is first paragraph <b>one</b></p>',
       '<p id="secondpara" align="center">This is senond paragraph <b>two</b></p></body>',
       '</html>']

# 合并四个字符串成一个大的html信息
#注意：这里需要在构造函数中手动设置一个解释器html.parser
soup = BeautifulSoup(''.join(doc), "html.parser")
#print(soup)

print(soup.findAll('p', align="center")[0])
