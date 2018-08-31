# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np


def foo(x, y):
    return x + y, x - y, x * y
a, b = 3, 4
c, d, e = foo(a, b)
print(c, d, e)
f, g = np.array([5, 6, 7]), np.array([8, 9, 10])
'''
h, i, j = [], [], []
for x, y in zip(f, g):
    add, sub, mul = foo(x, y)
    h.append(add)
    i.append(sub)
    j.append(mul)
h = np.array(h)
i = np.array(i)
j = np.array(j)
'''
uf = np.frompyfunc(foo, 2, 3)
print(type(uf))
h, i, j = uf(f, g)
print(h, i, j)
