# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
import matplotlib.pyplot as mp
outcomes = np.random.binomial(9, 0.5, 10000)
chips = [1000]
for outcome in outcomes:
    if outcome >= 5:
        chips.append(chips[-1] + 1)
    else:
        chips.append(chips[-1] - 1)
chips = np.array(chips)
mp.figure('Binomial Distribution',
          facecolor='lightgray')
mp.title('Binomial Distribution', fontsize=20)
mp.xlabel('Round', fontsize=14)
mp.ylabel('Chip', fontsize=14)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
o, h, l, c = 0, chips.argmax(), chips.argmin(), \
    chips.size - 1
if chips[o] < chips[c]:
    color = 'orangered'
elif chips[c] < chips[o]:
    color = 'limegreen'
else:
    color = 'dodgerblue'
mp.plot(chips, c=color, label='Chip')
mp.axhline(y=chips[o], linestyle='--',
           color='deepskyblue', linewidth=1)
mp.axhline(y=chips[h], linestyle='--',
           color='crimson', linewidth=1)
mp.axhline(y=chips[l], linestyle='--',
           color='seagreen', linewidth=1)
mp.axhline(y=chips[c], linestyle='--',
           color='orange', linewidth=1)
mp.scatter(o, chips[o], edgecolor='deepskyblue',
           facecolor='none', s=60,
           label='Opening: %d' % chips[o], zorder=3)
mp.scatter(h, chips[h], edgecolor='crimson',
           facecolor='none', s=60,
           label='Highest: %d' % chips[h], zorder=3)
mp.scatter(l, chips[l], edgecolor='seagreen',
           facecolor='none', s=60,
           label='Lowest: %d' % chips[l], zorder=3)
mp.scatter(c, chips[c], edgecolor='orange',
           facecolor='none', s=60,
           label='Closing: %d' % chips[c], zorder=3)
mp.legend()
mp.show()
