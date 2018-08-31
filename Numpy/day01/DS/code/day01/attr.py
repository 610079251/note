# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
a = np.array([[1 + 1j, 2 + 4j, 3 + 7j],
              [4 + 2j, 5 + 5j, 6 + 8j],
              [7 + 3j, 8 + 6j, 9 + 9j]])
print(a.dtype)
print(a.shape)
print(a.ndim, len(a.shape))
print(a.size, a.shape[0] * a.shape[1])
print(a.itemsize, int(128 / 8))
print(a.nbytes, a.size * a.itemsize)
print(a.T, a.transpose(), sep='\n')
print(a.real, a.imag, sep='\n')
for elem in a.flat:
    print(elem)
b = [100, 200, 300, 100, 200]
print(b)
c = np.array(b)  # list->ndarray
print(c)
d = list(c)  # ndarray->list
print(d)
e = tuple(c)  # ndarray->tuple
print(e)
f = set(c)  # ndarray->set
print(f)
