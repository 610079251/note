# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
a = np.matrix([[1, 2, 3],
               [4, 5, 6],
               [7, 8, 9]])
print(a, type(a))
b = np.arange(1, 10).reshape(3, 3)
print(b, type(b))
c = np.matrix(b)
print(c, type(c))
d = np.matrix('1 2 3; 4 5 6; 7 8 9')
print(d, type(d))
print('d:', id(d))
e = d
print('e:', id(e))
f = np.mat(e)
print('f:', id(f))
g = np.matrix(f, copy=False)
print('g:', id(g))
h = np.matrix(g)
print('h:', id(h))
d += 10
print(d, e, f, g, h, sep='\n')
print(b ** 2, b.dot(b), sep='\n')
#
# 1 2 3   1 2 3    1  4  9
# 4 5 6 x 4 5 6 = 16 25 36
# 7 8 9   7 8 9   49 64 81
#
print(h ** 2)
#
#             1   2   3
#     x       4   5   6
#             7   8   9
# 1   2   3  30  36  42
# 4   5   6  66  81  96
# 7   8   9 102 126 150
#
print(b.T, h.T, sep='\n')
i = np.mat('1 2 6; 3 5 7; 4 8 9')
j = i.I
print(j)
print(j * i)
k = np.ones((2, 2))
l = k * 2
m = k * 3
n = k * 4
print(k, l, m, n, sep='\n')
o = np.bmat('k l; m n')
print(o)
