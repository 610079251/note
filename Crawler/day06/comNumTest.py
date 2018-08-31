# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 14:20:47 2018

@author: Administrator
"""
# 递归方法去解组合数
def comNum(m,n):
    # C(m,0) = C(m,m) = 1
    if n==0 or n==m:
        return 1
    # C(m,n)=C(m-1,n-1)+C(m-1,n)
    return comNum(m-1, n-1)+comNum(m-1, n)

#print(comNum(3,2))
#print(comNum(3,1))
print(comNum(6,4)) #6!/(4!*2!) = 15
    