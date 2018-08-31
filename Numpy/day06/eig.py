# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
A = np.mat('3 -2; 1 0')
print(A)
eigvals, eigvecs = np.linalg.eig(A)
print(eigvals, eigvecs, sep='\n')
a = eigvals[0]
x = eigvecs[:, 0]
print(A * x, a * x, sep='\n')
a = eigvals[1]
x = eigvecs[:, 1]
print(A * x, a * x, sep='\n')
