# -*- encoding: utf-8 -*-
'''
@File : Runtime.py
@Time : 2020/04/12 11:40:58
@Author : zjm 
@Version : 3.7.6
@Contact : 1005564803@qq.com
@WebSite : https://github.com/sum-123/Python-.git
'''

# here put the import lib
import time
def add_log(func):   
    def wrapper(*args):
        start_time = time.time()
        func(*args)
        end_time = time.time()
        print("函数运行时间为",end_time-start_time)
        
    return wrapper
@add_log
def add(x,y):
    print(x+y)

add(1,10)