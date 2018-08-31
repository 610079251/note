# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
a = np.array([10, 20, -30, 40, -50])
b = np.array([60, -70, -80, -90, -100])
#c = a ^ b
#c = a.__xor__(b)
c = np.bitwise_xor(a, b)
print(c)
print(a[c < 0], b[c < 0], sep='\n')
d = np.arange(1, 21)
print(d)
print(d[d & (d - 1) == 0])
print(d[d.__and__(d - 1) == 0])
print(d[np.bitwise_and(d, (d - 1)) == 0])
