# -*- encoding: utf-8 -*-
'''
@File : 4contact.py
@Time : 2020/05/01 11:06:46
@Author : zjm 
@Version : 3.7.6
@Contact : 1005564803@qq.com
@WebSite : https://github.com/sum-123/Python-.git
'''

# here put the import lib

import time
import os
from multiprocessing import Process, Queue
def writer(q, message):
    print("writer：",os.getpid())
    q.put(message)
    print("发送信息：",message)
    time.sleep(1)

def reader(q):
    print("Reader",os.getpid())
    while True:
        message = q.get(True)
        print("收到信息",message)

def main():
    message = input("输入信息：")
    q = Queue()
    p = Process(target = writer, args = (q, message,))
    p_read = Process(target = reader, args = (q,))
    p.start()
    p_read.start()
    p.join()
    p_read.terminate()
main()