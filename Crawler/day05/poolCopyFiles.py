# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 11:11:00 2018

@author: Administrator
"""
#使用多进程或多线程去把一个
#文件夹下面的至少1000多个文件拷贝到另一
#个文件夹下面（这里暂不考虑文件夹中包含
#文件夹的情况）：
#A.文件类型要多样；
#B.怎么证明你拷贝的文件是正确的(HASH)；

import hashlib
import os
from multiprocessing import Pool
from multiprocessing import Manager


READMAXLENGTH = 2048
def copyFile(fileName, srcPath, destPath, q):
    """
    拷贝一个文件
    """
    srcFileName = srcPath+'/'+fileName
    destFileName = destPath+'/'+fileName
    with open(srcFileName, 'rb') as fr:
        with open(destFileName, 'wb') as fw:
            for i in fr:
                fw.write(i)
                
    q.put(fileName) #生产者生产的角色
    return True   

def hashFile(fileName):
    """
    对文件进行HASH
    """
    h = hashlib.sha256()#创建一个sha256的HASH算法对象
    #打开一个文件
    with open(fileName, 'rb') as f:
        while True:
            chunk = f.read(READMAXLENGTH)
            if not chunk:#说明文件读完
                break
            h.update(chunk)
    return h.hexdigest()

if __name__ == "__main__":
    isContiune = True
    # 得到原路径与目标路径
    srcPath = input("请输入您要拷贝的文件夹目录:")
    destPath = srcPath+"-副本"
    
    # 注意：这里需要循环执行，保证这个文件夹不存在
    #否则会覆盖原数据
    while os.path.exists(destPath):
        destPath = destPath+"-副本"
    
    # 如果目标文件夹不存在，需要创建
    if not os.path.exists(destPath):
        try:
            os.mkdir(destPath)
        except:
            print("mkdir %s error"%destPath)
            isContiune = False
        
    # 如果源文件夹不存在
    if not os.path.exists(srcPath):
        print("strPath %s is not exists"%srcPath)
        isContiune = False
       
    if isContiune == True:
        # 记录文件个数信息，以便将来可以做进度条
        allFiles = os.listdir(srcPath)
#        for i in allFiles:
#            srcFileName = srcPath+'/'+i
#            destFileName = destPath+'/'+i
#            copyFile(srcFileName,destFileName)
#            # HASH检查
#            if hashFile(srcFileName) != hashFile(destFileName):
#                print("copy file Error")
        allNum = len(allFiles)
        num = 0 # 记录当前的进度
        
        p = Pool()
        q = Manager().Queue()
        for i in allFiles:
            p.apply_async(func=copyFile,args=(i,srcPath,destPath,q))
        p.close()
        
        while num < allNum:
            fileName = q.get()#消费者
            rate = num/allNum*100
                      
            num += 1#当前进度+1
            srcFileName = srcPath+'/'+fileName
            destFileName = destPath+'/'+fileName
            if hashFile(srcFileName) != hashFile(destFileName):
                print("%s copy file Error"%srcFileName)
                
            print("Current Rate is %.1f%%"%rate)
   
    p.join()
    print("over")

#print(copyFile('C:/Users/Administrator/Desktop/网络爬虫1/网络爬虫1/网络爬虫/day05/captcha.7z',
#         'C:/Users/Administrator/Desktop/网络爬虫1/网络爬虫1/网络爬虫/day05/captcha2.7z'))
#print(hashFile('C:/Users/Administrator/Desktop/网络爬虫1/网络爬虫1/网络爬虫/day05/captcha.7z') ==
#      hashFile('C:/Users/Administrator/Desktop/网络爬虫1/网络爬虫1/网络爬虫/day05/captcha2.7z'))