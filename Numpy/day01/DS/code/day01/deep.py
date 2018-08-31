# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
a = np.arange(11, 20).reshape(3, 3)
print(a)
b = a + 10
print(b)
c = np.dstack((a, b))
print(c)
d, e = np.dsplit(c, 2)
print(d.T[0].T, e.T[0].T, sep='\n')
