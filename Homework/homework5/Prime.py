# -*- encoding: utf-8 -*-
'''
@File : Prime.py
@Time : 2020/04/14 15:24:11
@Author : zjm 
@Version : 3.7.6
@Contact : 1005564803@qq.com
@WebSite : https://github.com/sum-123/Python-.git
'''

# here put the import lib
li=[]
def outer(func):
   
    def prime():
        count=0
        m=int(input('left'))
        n=int(input('right'))
        for num in range(m,n+1):
            if num>1:
                for i in range(2,num):
                    if(num % i) == 0:
                        break
                else:
                     li.append(num)
                     count+=1
        return func(count)

    return prime
@outer
def Primeprint(count):
    print(li)
Primeprint()

@outer
def Primeprint(count):
    print(li)
    print('共有%d个素数'%count)
Primeprint()