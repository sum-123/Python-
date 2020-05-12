# -*- encoding: utf-8 -*-
'''
@File : test6.py
@Time : 2020/05/02 16:15:47
@Author : zjm 
@Version : 3.7.6
@Contact : 1005564803@qq.com
@WebSite : https://github.com/sum-123/Python-.git
'''
# 编写一个接收数据的网络程序，由“网络调试工具”发送数据，你的程序接收数据并打印输出
# here put the import lib
from socket import *

def main():
   # 绑定端口信息
    udp_socket=socket(AF_INET,SOCK_DGRAM)
    local_addr=('127.0.0.1',9999)

    udp_socket.bind(local_addr)
   # 接收数据
    recv_data = udp_socket.recvfrom(1024)
   # 打印显示接收到的数据
    print(recv_data[0].decode('utf-8')[:])
   # 关闭套接字
    udp_socket.close()

if __name__ == "__main__":
    main()