# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
M = np.mat('4 11 14; 8 7 -2')
print(M)
U, sv, V = np.linalg.svd(M, full_matrices=False)
print(U, sv, V, sep='\n')
print(U * U.T, V * V.T, sep='\n')
Sigma = np.diag(sv)
print(Sigma)
print(U * Sigma * V)
