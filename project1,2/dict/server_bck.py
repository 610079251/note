#!/usr/bin/env python3
#coding=utf-8 

'''
name:Levi
MODULES:　python3.5  mysql  pymysql
This is a dict project for AID 
'''

from socket import *
import os 
import signal 
import time 
import sys
import pymysql 


#设定服务器IP.端口号
HOST = '127.0.0.1'
PORT = 8000
ADDR = (HOST,PORT)
DICT_TEXT = "./dict.txt"  #文本路径

#主控制流程
def main():
    #数据库链接
    db = pymysql.connect('localhost','root','123456','dict')

    #创建tcp套接字
    s = socket()
    #设置端口号立即释放
    s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    #绑定IP和端口
    s.bind(ADDR)
    #设定服务器可连接数量
    s.listen(5)
    #忽略子进程退出
    signal.signal(signal.SIGCHLD,signal.SIG_IGN)

    #创建循环,创建父进程循环等待连接,子进程处理客户端请求
    while True:
        #尝试捕获连接错误
        try:
            #等待客户端连接
            c,addr = s.accept()
            #客户端连接成功,打印客户端地址
            print("Connect from",addr)
        #捕获到键盘信号ctrl+c退出服务器
        except KeyboardInterrupt:
            sys.exit("服务器退出")      
        #其他错误捕获后不处理,直接循环等待下次连接
        except Exception:
            continue 

        #创建子进程
        pid = os.fork()
        #子进程中把无用的
        if pid == 0:
            s.close()
            do_child(c,db)
        else:
            c.close()
            continue  

def do_child(c,db):
    #循环接收客户请求
    while True:
        data = c.recv(128).decode()
        print("Request:",data)

        if data[0] == 'R':
            do_register(c,db,data)
        elif data[0] == 'L':
            do_login()
        elif data[0] == 'E':
            c.close()
            sys.exit(0)
        elif data[0] == 'Q':
            do_query()
        elif data[0] == 'H':
            do_history()


def do_register(c,db,data):
    print(">>>>>执行注册操作<<<<<")
    l = data.split(' ')
    name = l[1]
    passwd = l[2]

    cursor = db.cursor()

    #判断是否name是否存在
    sql = "select name from user where name='%s'"%name
    cursor.execute(sql)
    r = cursor.fetchone()
    if r != None:
        c.send(b"EXISTS")
        return 

    #插入到数据库
    sql = "insert into user (name,passwd) values ('%s','%s')"%(name,passwd)
    try:
        cursor.execute(sql)
        db.commit()
        c.send(b'OK')
    except:
        c.send(b"FALL")
        db.rollback()
        return 
    else:
        print("注册成功")

def do_login():
    pass 

def do_query():
    pass 

def do_history():
    pass 


if __name__ == "__main__":
    main()


