# -*- encoding: utf-8 -*-
'''
@File : BubbleSort.py
@Time : 2020/03/09 21:18:45
@Author : zjm 
@Version : 1.0
@Contact : 1005564803@qq.com
@WebSite : https://github.com/sum-123/Python-.git
'''

# here put the import lib
from random import randint
def Bubblesort(n):
    temp=0
    for i in range(len(n)):
        for j in range(len(n)-1):
            if n[j]>n[j+1]:
                temp=n[j]
                n[j]=n[j+1] 
                n[j+1]=temp
list=[randint(1,100) for _ in range(20)]
Bubblesort(list)
print(list)
