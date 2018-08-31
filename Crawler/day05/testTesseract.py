# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 17:48:11 2018

@author: Administrator
"""

from PIL import Image
from pytesseract import *
# 加载图片
image = Image.open('test4.jpg')
# 识别过程
text = image_to_string(image)
print(text)
