# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
A = np.mat('1 2 3; 8 9 4; 7 6 5')
print(A)
B = np.linalg.inv(A)
print(B)
C = np.linalg.inv(B)
print(C)
D = A * B
print(D)
E = np.mat('0 1 2 3; 0 8 9 4; 0 7 6 5')
print(E)
#F = np.linalg.inv(E)
F = E.I
print(F)
print(E * F)
