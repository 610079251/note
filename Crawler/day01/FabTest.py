# -*- coding: utf-8 -*-
"""
Created on Tue Aug  7 14:14:23 2018

@author: Administrator
"""

#		斐波那契数列：1,1,2,3,5,8,13,21,34...
#f(n) = f(n-1)+f(n-2) n >= 2
#              1      0<= n <2
def Fab(n):
    assert(type(n) == type(1))
    if 0 <= n < 2:
        return 1
    else:# 注意：这里Fab自己调自己，是递归
        return Fab(n-1)+Fab(n-2)

for i in range(0, 9):#0,1,2,...,8
    print(Fab(i))
#Fab('a')
    
