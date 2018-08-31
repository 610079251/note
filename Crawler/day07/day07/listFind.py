# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 14:16:34 2018

@author: Administrator
"""

def findNum(L1, L2):
    """
    快速的找出两个List中丢失的那个数。
    """
    for i in range(max(len(L1),len(L2))):
        if L1[i] != L2[i]:
            if len(L1) >= len(L2):
                return L1[i]
            return L2[i]


def findNum2(L1,L2):
    """
    快速的找出两个List中丢失的那个数。
    """
    sum1 = sum(L1)
    sum2 = sum(L2)
    if sum1 > sum2:
        return sum1-sum2
    else:
        return sum2-sum1


def removeSameV(L):
    """
    把一个list中重复的元素去除
    """
    L = list(set(L))
    return L

def removeSameV2(L):
    """
    把一个list中重复的元素去除
    """
    myDict = {}
    for i in L:
        myDict[i] = 0
    L = list(myDict.keys())
    return L

def removeSameV3(L):
    """
    把一个list中重复的元素去除
    """
    L1 = []
    for i in L:
        if i not in L1:
            L1.append(i)
    return L1


L = [3,2,1,2,3,4,5]
print(removeSameV(L))
print(removeSameV2(L))
print(removeSameV3(L))

#L1 = [1,7,2,5,3,6,9]
#L2 = [1,2,7,5,6,9]
#print(findNum2(L1,L2))
#assert(findNum(L1, L2) == 3)






