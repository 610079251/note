# -*- coding: utf-8 -*-
"""
Created on Wed Aug  8 09:22:24 2018

@author: Administrator
"""
#递归的方法：
#	1)基准点；比如面试题中的list只有1个或2个元素的情况；
#	2)找到一个递推公式或者分解这个问题的方法，让原来问题
#的规模变小，变简单；比如面试题中把list中的元素
#分解成两部分：左半部分和右半部分；
#leftPart:   max1,min1
#rightPart:  max2,min2
#最终结果;maxV = max(max1,max2)
#         minV = min(min1,min2)

#在一个list中，有一堆数，请用递归方法求出这堆数的最大最小值；
#[1,3,7,5,4,2,6,10,0.2,-10]
def _minMax(L, start, end):
    """
    在一个list中，有一堆数，请用递归方法求出这堆数的最大最小值
    """
    ##start+(end-start)//2 --> (end+start)//2
    if end-start <= 1:
        return (max(L[start],L[end]),min(L[start],L[end]))
    else:
        max1,min1 = _minMax(L,start,(end+start)//2)
        max2,min2 = _minMax(L,(end+start)//2+1,end)
        return (max(max1,max2), min(min1,min2))
# 1,2,3,4,5
# 1,2,3,4
def minMax(L):
    assert(len(L) > 0)
    return _minMax(L, 0, len(L)-1) 
    
L = [1,3,7,5,4,2,6,10,0.2,-10]
#L = []
print(minMax(L))
    
    
