# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
print(type(np.add))
a = np.array([10, 20, 30])
b = np.array([1,  2,  3])
c = np.add(a, b)
print(c)
d = a + b
print(d)
e = np.add.reduce(a)
print(e)
f = np.add.accumulate(a)
print(f)
g = np.arange(1, 7)
print(g)
#
# 1 2 3 4 5 6
# 0 1 2 3 4 5
# ^   ^   ^
#
h = np.add.reduceat(g, [0, 2, 4])
print(h)
i = np.add.outer(a, b)
print(i)
#
#  +  1  2  3
# 10 11 12 13
# 20 21 22 23
# 30 31 32 33
#
j = np.outer(a, b)  # 外积
print(j)
#
#  x  1  2  3
# 10 10 20 30
# 20 20 40 60
# 30 30 60 90
#
