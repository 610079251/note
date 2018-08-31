# -*- coding: utf-8 -*-
"""
Created on Wed Aug  8 17:16:52 2018

@author: Administrator
"""

from lxml import etree

xml = """
<bookstore>
<book>
  <title lang="en">Harry Potter</title>
  <author>J K. Rowling</author> 
  <year>2005</year>
  <price>29.99</price>
</book>
<book>
  <title lang="chs">Python爬虫</title>
  <author>Joe</author> 
  <year>2018</year>
  <price>39.99</price>
</book>
</bookstore>
"""

root = etree.fromstring(xml)
#print(root)

# 取节点
elements = root.xpath("book")
#print(elements)
#for element in elements:

# 打印文本书名
#for element in elements:
#    print(element.getchildren()[0].text)
#
## 打印属性
#for element in elements:
#    print(element.getchildren()[0].attrib['lang'])
    
#XPath来取属性
elements = root.xpath('//@lang')
print(elements)

