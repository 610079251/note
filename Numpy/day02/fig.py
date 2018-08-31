# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
import matplotlib.pyplot as mp
x = np.linspace(-np.pi, np.pi, 1000)
cos_y = np.cos(x) / 2
sin_y = np.sin(x)
mp.figure('Sin', figsize=(6, 4), dpi=120,
          facecolor='dodgerblue')
mp.title('Sin', fontsize=20)
mp.xlabel('x', fontsize=14)
mp.ylabel('y=sin(x)', fontsize=14)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.figure('Cos', figsize=(6, 4), dpi=120,
          facecolor='limegreen')
mp.title('Cos', fontsize=20)
mp.xlabel('x', fontsize=14)
mp.ylabel('y=cos(x)', fontsize=14)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.figure('Sin')
mp.plot(x, sin_y, c='orangered',
        label=r'$y=sin(x)$')
mp.legend()
mp.figure('Cos')
mp.plot(x, cos_y, c='orangered',
        label=r'$y=\frac{1}{2}cos(x)$')
mp.legend()
mp.show()
