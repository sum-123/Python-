# -*- encoding: utf-8 -*-
'''
@File : Outoddnum.py
@Time : 2020/03/09 17:24:10
@Author : zjm 
@Version : 1.0
@Contact : 1005564803@qq.com
@WebSite : https://github.com/sum-123/Python-.git
'''

# here put the import lib
from random import randint
def fun(n):
    for i in n:
        if i%2!=0:
            print(i,end=' ')
   
list1=[randint(1,100) for _ in range(30)]
print(list1)#输出随机列表
fun(list1)#输出列表中的奇数