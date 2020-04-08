# -*- encoding: utf-8 -*-
'''
@File : test2.py
@Time : 2020/04/03 10:05:57
@Author : zjm 
@Version : 3.7.6
@Contact : 1005564803@qq.com
@WebSite : https://github.com/sum-123/Python-.git
'''

# here put the import lib
def add_log(func):
    def wrapper(*args):
        res = func(*args)
        print('进行了加法计算')
        return res
    return wrapper
@add_log
def add(x,y):
    print(x+y)
add(1,10)

