# -*- coding: utf-8 -*-
"""
Created on Thu Aug  9 16:21:46 2018

@author: Administrator
"""

def Fab(N):
    """
    使用把第N个斐波那契数列的值打印出来
    """
    a,b=0,1
    for _ in range(N):#0-7
        a,b=b,a+b 
        yield a #会把a此时的值返回给调用方，同时保存当前函数的执行状态,
                #并把当前CPU的时间片给调用方
    #return a
#0: a=0,b=1 --> a=1,b=1
#1: a=1,b=1 --> a=1,b=2
#2: a=1,b=2 --> a=2,b=3
#3: a=2,b=3 --> a=3,b=5
#...
#7: a=13,b=21--> a=21,b=34

if __name__ == "__main__":
#    for i in range(1,9):
#        print(Fab(i))#1,1,2,3,5,8,13,21
    f = Fab(8)
    print(next(f)) # 1
    print(next(f)) # 1
    print(next(f)) # 2
    print(next(f)) # 3
    print(next(f)) # 5
    print(next(f)) # 8
    print(next(f)) # 13
    print(next(f)) # 21
    #print(next(f))