# -*- encoding: utf-8 -*-
'''
@File : Printtxt.py
@Time : 2020/03/26 19:55:40
@Author : zjm 
@Version : 3.7.6
@Contact : 1005564803@qq.com
@WebSite : https://github.com/sum-123/Python-.git
'''

# here put the import lib
import os
def read():
    List=[]
    try:
        f=open("/Users/zhaojiaming/Documents/GitHub/Python-/Homework/homework3/input.txt","rt")
        while True:
            t=f.readline()
            if not t:
                f.close()
                return List
            t=t.rstrip()
            List.append(t)
    except IOError:
        print("打开失败")
def print_f(List):
    for i,t in enumerate(List,1):
        print("第{}行 : {}".format(i,t))
print_f(read())

 

