#tcp_server.py 
from socket import *  

#创建套接字
sockfd = socket(AF_INET,SOCK_STREAM)

#绑定地址
sockfd.bind(('172.60.50.50',9999))

#设置监听
sockfd.listen(5)

print("Waiting for connect....")
#阻塞等待客户端请求
connfd,addr = sockfd.accept()
print("Connect from",addr)

#接收消息
data = connfd.recv(1024)
print("Receive message:",data.decode())

#发送消息　
n = connfd.send(b'I love China')
print("发送了%d个字节"%n)

#关闭套接字
connfd.close()
sockfd.close()


