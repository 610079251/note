# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
closing_prices = np.loadtxt(
    '../../data/aapl.csv', delimiter=',',
    usecols=(6), unpack=True)
mean = closing_prices.mean()  # 算数平均值
devs = closing_prices - mean  # 离差
dev2 = devs ** 2  # 离差方
pvar = dev2.mean()  # 总体方差
svar = dev2.sum() / (dev2.size - 1)  # 样本方差
pstd = np.sqrt(pvar)  # 总体标准差
sstd = np.sqrt(svar)  # 样本标准差
print(pstd, sstd)
pstd = np.std(closing_prices)
sstd = np.std(closing_prices, ddof=1)
print(pstd, sstd)
