# -*- coding: utf-8 -*-
"""
Created on Fri Aug 10 14:14:52 2018

@author: Administrator
"""
def reverse(str_list,start,end):
    while start<end:
        str_list[start],str_list[end]=str_list[end],str_list[start]
        start += 1
        end -= 1
        
def reverseSenten(s):
    """
    输入一个英文句子，翻转句子中单词的顺序，
但单词内字符的顺序不变。
    """
    str_list = list(s)
    i = 0
    ll = len(str_list)
    while i < ll:
        if str_list[i] != " ":
            start = i
            end =start +1
            while(end<ll) and (str_list[end] != " "):
                end += 1
            reverse(str_list,start,end-1)
            i = end
        else:
            i +=1
    str_list.reverse()
    return(''.join(str_list))
    
#    l1 = s.split()
#    #l2 = []
#    #l2.extend(l1) #注意append与extend的区别
#    while len(l1) > 0:
#        print(l1.pop(), end=" ")
    

    

#s = "I am a student ."
s = "how are you"
result = reverseSenten(s)
print(result)
#assert(result == "student. a am I")


