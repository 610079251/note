# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
a = np.arange(1, 9)
print(a)
b = a.reshape(2, 4)
#b = a.reshape(2, 4).copy()
print(b)
c = b.reshape(2, 2, 2)
print(c)
d = c.ravel()
print(d)
e = c.flatten()
print(e)
a += 10
print(a, b, c, d, e, sep='\n')
a.shape = (2, 4)
print(a)
a.resize(4, 2)
print(a)
f = a.transpose()
print(f)
f -= 10
print(a)
