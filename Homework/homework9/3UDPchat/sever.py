# -*- encoding: utf-8 -*-
'''
@File : sever.py
@Time : 2020/05/04 08:33:42
@Author : zjm 
@Version : 3.7.6
@Contact : 1005564803@qq.com
@WebSite : https://github.com/sum-123/Python-.git
'''

# here put the import lib
from socket import *

host = ''  #服务器地址
port = 12345  #服务器端口
bufsiz = 2048 #缓存大小
adds = (host, port) #地址+端口

udpsersock = socket(AF_INET, SOCK_DGRAM)  #创建UDP的套接字类型。
udpsersock.bind(adds)  #绑定到地址和端口

while True:
    msg = input('服务器speak：')   
    data, addc = udpsersock.recvfrom(bufsiz)
    udpsersock.sendto(msg.encode('utf-8'), addc)
    
    if not data: break
    print('客户端reply：', data.decode('utf-8'))
    
udpsersock.close()
