# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import matplotlib.pyplot as mp
import matplotlib.gridspec as mg
mp.figure('GridSpec', facecolor='lightgray')
gs = mg.GridSpec(3, 2)
mp.subplot(gs[0, :])
mp.xticks(())
mp.yticks(())
mp.text(0.5, 0.5, '1', ha='center', va='center',
        size=36, alpha=0.5)
mp.subplot(gs[1:, 0])
mp.xticks(())
mp.yticks(())
mp.text(0.5, 0.5, '2', ha='center', va='center',
        size=36, alpha=0.5)
mp.subplot(gs[1, 1])
mp.xticks(())
mp.yticks(())
mp.text(0.5, 0.5, '3', ha='center', va='center',
        size=36, alpha=0.5)
mp.subplot(gs[2, 1])
mp.xticks(())
mp.yticks(())
mp.text(0.5, 0.5, '4', ha='center', va='center',
        size=36, alpha=0.5)
mp.tight_layout()
mp.show()
