# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
# 产生位于[10, 100)区间的随机整数
a = np.random.randint(10, 100, 9).reshape(3, 3)
print(a)
b, c = np.max(a), np.min(a)
print(b, c)
d, e = np.argmax(a), np.argmin(a)
print(d, e)
f = np.random.randint(10, 100, 9).reshape(3, 3)
print(f)
g, h = np.maximum(a, f), np.minimum(a, f)
print(g, h, sep='\n')
