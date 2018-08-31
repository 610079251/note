# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
a = np.arange(11, 20).reshape(3, 3)
print(a)
b = a + 10
print(b)
#c = np.hstack((a, b))
c = np.concatenate((a, b), axis=1)
print(c)
#d, e, f = np.hsplit(c, 3)
d, e, f = np.split(c, 3, axis=1)
print(d, e, f, sep='\n')
