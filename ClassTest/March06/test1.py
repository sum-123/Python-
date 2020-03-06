# -*- encoding: utf-8 -*-
'''
@File : test1.py
@Time : 2020/03/06 08:27:09
@Author : zjm 
@Version : 1.0
@Contact : 1005564803@qq.com
@WebSite : https://github.com/sum-123/Python-.git
'''

# here put the import lib
def computate():
    m=int(input("请输入水果重量"))
    n=int(input("请输入苹果的单价"))
    print("水果的价格是")
    x=m*n
    print(x)
computate()


def myfun():
    print('this is my function')
myfun()
def ChangeInt( a ):
    print("a重新赋值前的地址",id(a))
    a = 10
    print("a重新赋值后的值",a)
    print("a重新赋值后的地址",id(a))
b = 2
print("b的地址",id(b))
ChangeInt(b)
print("传了参数后b的地址",id(b))
print( 'b的值',b ) 