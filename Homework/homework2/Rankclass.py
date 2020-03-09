# -*- encoding: utf-8 -*-
'''
@File : Rankclass.py
@Time : 2020/03/09 20:41:57
@Author : zjm 
@Version : 1.0
@Contact : 1005564803@qq.com
@WebSite : https://github.com/sum-123/Python-.git
'''

# here put the import lib
from random import randint
def rankclass(n):
    for i in n:
        if i>=90:
            print(i,'成绩为','A')
        elif i>=80 and i<90:
            print(i,'成绩为','B')
        elif i>=70 and i<80:
            print(i,'成绩为','C')
        else:
            print(i,'成绩为','D')
list1=[randint(50,100) for _ in range(20)]
rankclass(list1)