# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
import matplotlib.pyplot as mp
x = np.linspace(-np.pi, np.pi, 1000)
cos_y = np.cos(x) / 2
sin_y = np.sin(x)
mp.xlim(x.min(), x.max())
mp.ylim(sin_y.min(), sin_y.max())
mp.plot(x, cos_y, linestyle='--', linewidth=0.5,
        color='red')
mp.plot(x, sin_y, linestyle=':', linewidth=6,
        color='green')
mp.show()
