# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
a = np.array(['A', 'B', 'C'])
b = np.array(['D', 'E', 'F'])
#c = np.row_stack((a, b))
c = np.vstack((a, b))
print(c)
#d = np.column_stack((a, b))
#d = np.hstack((a.reshape(-1, 1), b.reshape(-1, 1)))
d = np.c_[a, b]
print(d)
