# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
a = np.arange(1, 6)
print(a)
b = a.clip(min=2, max=4)
print(b)
c = a.compress((2 <= a) & (a <= 4))
print(c)
d = a.prod()
print(d)
e = a.cumprod()
print(e)


def jiecheng(n):
    return 1 if n == 1 else n * jiecheng(n - 1)
print(jiecheng(5))
print((np.arange(5) + 1).prod())
