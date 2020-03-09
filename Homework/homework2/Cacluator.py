# -*- encoding: utf-8 -*-
'''
@File : Cacluator.py
@Time : 2020/03/09 21:35:00
@Author : zjm 
@Version : 1.0
@Contact : 1005564803@qq.com
@WebSite : https://github.com/sum-123/Python-.git
'''

# here put the import lib
def Cacluate(m,n,t):
    if t=='*':
        return m*n
    elif t=='/':
        return m/n
    elif t=='-':
        return m-n 
    elif t=='+':
        return m+n

m=int(input('请输入第一个数'))
t=input('请输入运算符')
n=int(input('请输入第二个数'))
print(m,t,n,'=',Cacluate(m,n,t))
