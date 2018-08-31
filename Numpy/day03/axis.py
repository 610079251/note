# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np


def foo(x):
    print('foo:', x)
    return x.sum(), x.mean(), x.std()


a = np.array([1, 2, 3, 4, 5])
print(foo(a))
b = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])
print('-' * 40)
print(np.apply_along_axis(foo, 0, b))
print('-' * 40)
print(np.apply_along_axis(foo, 1, b))
