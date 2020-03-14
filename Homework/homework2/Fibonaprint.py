# -*- encoding: utf-8 -*-
'''
@File : Fibonaprint.py
@Time : 2020/03/09 20:32:48
@Author : zjm 
@Version : 1.0
@Contact : 1005564803@qq.com
@WebSite : https://github.com/sum-123/Python-.git
'''

# here put the import lib
def Fibonacci(n):
    a1=0
    a2=1
    a=1
    print(a2,end=' ')
    if(n==0):
        return 
    while a<=n:
        print(a,end=' ')
        a1=a2
        a2=a
        a=a1+a2
Fibonacci(100)


