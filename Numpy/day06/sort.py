# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
a = np.array(['Z3', 'L4', 'W5', 'Z6'])
b = np.array([27, 22, 25, 22])
c = np.array([170, 165, 175, 158])
print(np.lexsort((c, b)))
print(a[np.lexsort((c, b))])
d = b + c * 1j
print(d)
e = np.sort_complex(d)
print(e)
f = np.array([13, 11, np.nan, 19, 17])
print(np.nanmax(f), np.nanmin(f))
print(np.nanargmax(f), np.nanargmin(f))
#             0  1  2  3  4  5  6
g = np.array([1, 2, 4, 5, 6, 8, 9])
h = np.array([7, 3])
i = np.searchsorted(g, h)
print(i)
j = np.insert(g, i, h)
print(j)
