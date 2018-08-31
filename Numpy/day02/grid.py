# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
import matplotlib.pyplot as mp
mp.figure('Grid', facecolor='lightgray')
mp.title('Grid', fontsize=20)
mp.xlabel('x', fontsize=14)
mp.ylabel('y', fontsize=14)
mp.xlim(0, 10)
mp.ylim(0, 10)
ax = mp.gca()
ax.xaxis.set_major_locator(mp.MultipleLocator(1.0))
ax.xaxis.set_minor_locator(mp.MultipleLocator(0.1))
ax.yaxis.set_major_locator(mp.MultipleLocator(1.0))
ax.yaxis.set_minor_locator(mp.MultipleLocator(0.1))
mp.tick_params(labelsize=10)
mp.grid(which='major', axis='both', linewidth=0.75,
        linestyle='-', color='lightgray')
mp.grid(which='minor', axis='both', linewidth=0.25,
        linestyle='-', color='lightgray')
mp.show()
