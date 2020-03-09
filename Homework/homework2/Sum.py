# -*- encoding: utf-8 -*-
'''
@File : Sum.py
@Time : 2020/03/09 17:16:56
@Author : zjm 
@Version : 1.0
@Contact : 1005564803@qq.com
@WebSite : https://github.com/sum-123/Python-.git
'''

# here put the import lib
def sum(*args):
    total = 0
    for i in args:
        total += i
    return total
print(sum(1,2,3,8,23,6,8,7))