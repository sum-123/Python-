# -*- encoding: utf-8 -*-
'''
@File : test5.py
@Time : 2020/05/08 07:56:41
@Author : zjm 
@Version : 3.7.6
@Contact : 1005564803@qq.com
@WebSite : https://github.com/sum-123/Python-.git
'''

# here put the import lib
# import socket

# def main():
#     #1 创建一个udp套接字
#     udp_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    
#     # 2. 准备接收方的地址 使用udp套接字发送数据:发什么,发给谁
#     # '192.168.1.24'表示目的ip地址
#     # 8888表示目的端口
#     dest_addr = ('192.168.1.40', 8888)  # 注意 是元组，ip是字符串，端口是数字

#     # 3. 从键盘获取数据
#     send_data = input("请输入要发送的数据:")
#     # 4. 发送数据到指定的电脑上的指定程序中
#     udp_socket.sendto(send_data.encode('utf-8'), dest_addr)
    
#     # 5 关闭套接字
#     udp_socket.close()
   
# if __name__ == "__main__":
#     main()
# from socket import *

# def main():
#    # 绑定端口信息
#     udp_socket=socket(AF_INET,SOCK_DGRAM)
#     local_addr=('127.0.0.1',9999)

#     udp_socket.bind(local_addr)
#    # 接收数据
#     recv_data = udp_socket.recvfrom(1024)  # 1024表示本次接收的最大字节数
#    # 打印显示接收到的数据
#     print(recv_data)

#     print(recv_data[0].decode('utf-8'))
#     print(recv_data[1])

#    # 关闭套接字
#     udp_socket.close()

# if __name__ == "__main__":
#     main()
# import socket

# s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# # 绑定端口:
# s.bind(('127.0.0.1', 9999))

# print('Bind UDP on 9999...')

# while True:
#     # 接收数据:
#     data, addr = s.recvfrom(1024)
#     print('Received from %s:%s.' % addr)
#     reply = 'Hello, %s!' % data.decode('utf-8')
#     s.sendto(reply.encode('utf-8'), addr)
# import socket

# s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# s.bind(('127.0.0.1', 9999))
# for data in [b'Michael', b'Tracy', b'Sarah']:
#     # 发送数据:
#     s.sendto(data, ('127.0.0.1', 9999))
#     # 接收数据:
#     print(s.recv(1024).decode('utf-8'))

# s.close()
import socket
import sys

# 创建 socket 对象
serversocket = socket.socket(
            socket.AF_INET, socket.SOCK_STREAM) 

# 获取本地主机名
host = socket.gethostname()

port = 9999

# 绑定端口号
serversocket.bind((host, port))

# 设置最大连接数，超过后排队
serversocket.listen(5)

while True:
    # 建立客户端连接
    clientsocket,addr = serversocket.accept()      

    print("连接地址: %s" % str(addr))
    
    msg='欢迎访问菜鸟教程！'+ "\r\n"
    clientsocket.send(msg.encode('utf-8'))
    clientsocket.close()
#!/usr/bin/python3
# 文件名：client.py

# 导入 socket、sys 模块
import socket
import sys

# 创建 socket 对象
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

# 获取本地主机名
host = socket.gethostname() 

# 设置端口号
port = 9999

# 连接服务，指定主机和端口
s.connect((host, port))

# 接收小于 1024 字节的数据
msg = s.recv(1024)

s.close()

print (msg.decode('utf-8'))