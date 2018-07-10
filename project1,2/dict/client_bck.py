#!/usr/bin/env python3 
#coding=utf-8 

from socket import *
import sys 
import traceback
import getpass

#主控制流程函数
def main():
    if len(sys.argv) < 3:
        print('argv is error')
        return 
    host = sys.argv[1]
    port = int(sys.argv[2])

    s = socket()
    try:
        s.connect((host,port))
    except Exception:
        traceback.print_exc()
        return 

    while True:
        print('''
            =============Welcome============
            -- 1.注册　　2.登录　　 3.退出--
            ================================
            ''')
        try:
            cmd = int(input("请输入选项>>"))
        except Exception:
            print("命令错误！！")
            continue

        if cmd not in [1,2,3]:
            print("没有该选项！！")
            continue
        elif cmd == 1:
            if do_register(s) == 0:
                print("注册成功！可以登录")
            else:
                print("注册失败！")
        elif cmd == 2:
            do_login()
        elif cmd == 3:
            s.send(b'E')
            sys.exit("谢谢使用")

def do_register(s):
    while True:
        name = input("User:")
        passwd = getpass.getpass()
        passwd1 = getpass.getpass('Confirm:')

        if (' ' in name) or (' ' in passwd):
            print("用户名或密码不能有空格")
            continue 
        if passwd != passwd1:
            print("两次密码不一致")
            continue 

        #将注册信息发送给服务器
        msg = 'R {} {}'.format(name,passwd)
        s.send(msg.encode())

        data = s.recv(128).decode()
        print(data)
        if data == 'OK':
            return 0
        elif data == 'EXISTS':
            print("用户名已存在")
            return 1
        else:
            return 1


def do_login():
    pass 

if __name__ == "__main__":
    main()
