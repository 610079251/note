# -*- coding: utf-8 -*-
"""
Created on Fri Aug 10 17:37:04 2018

@author: Administrator
"""

import hashlib

def hashStr(strInfo):
    """
    对字符串做HASH
    """
    h = hashlib.sha256()#创建一个sha256的HASH算法对象
    h.update(strInfo.encode("utf-8"))#先转换成bytes
    return h.hexdigest()

def hashFile(fileName):
    """
    对文件进行HASH
    """
    h = hashlib.sha256()#创建一个sha256的HASH算法对象
    #打开一个文件
    with open(fileName, 'rb') as f:
        while True:
            chunk = f.read(2048)
            if not chunk:#说明文件读完
                break
            h.update(chunk)
    return h.hexdigest()
            

print(hashStr("hello world"))
#b94d27b9934d3e08a52e52d7da7dabfac484efe37a5380ee9088f7ace2efcde9
print(hashStr("hello python"))
#373a23512f9531ad49ec6ad43ecdda58df01e59d9ec5812d601fd05cc53345d3    
print(hashStr("hello world"))    
#b94d27b9934d3e08a52e52d7da7dabfac484efe37a5380ee9088f7ace2efcde9   
    
print(hashFile("baiduSearch.html"))
#358cad568263a3305d5c0fe4867cf33d4e880f0fe8a138a8dae99b760a055f2a    