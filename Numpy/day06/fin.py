# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
# 终值 = fv(利率, 期数, 每期支付, 现值)
# 将1000元以1%的利率存入银行5年，每年加存100元，
# 到期后本息合计多少钱？
fv = np.fv(0.01, 5, -100, -1000)
print(round(fv, 2))
# 现值 = pv(利率, 期数, 每期支付, 终值)
# 将多少钱以1%的利率存入银行5年，每年加存100元，
# 到期后本息合计共fv元？
pv = np.pv(0.01, 5, -100, fv)
print(round(pv, 2))
# 净现值 = npv(利率, 现金流)
# 将1000元以1%的利率存入银行5年，每年加存100元，
# 相当于一次存入多少钱？
npv = np.npv(0.01,
             [-1000, -100, -100, -100, -100, -100])
print(round(npv, 2))
fv = np.fv(0.01, 5, 0, npv)
print(round(fv, 2))
# 内部收益率 = irr(现金流)
# 将1000元存入银行5年，以后逐年提现100元、200元、
# 300元、400元、500元，银行年利率达到多少，可在
# 最后一次提现后偿清全部本息？即使净现值为0的利率。
irr = np.irr([-1000, 100, 200, 300, 400, 500])
print(round(irr, 2))
npv = np.npv(irr, [-1000, 100, 200, 300, 400, 500])
print(round(npv, 2))
