# -*- encoding: utf-8 -*-
'''
@File : Countstr_max.py
@Time : 2020/03/09 20:52:43
@Author : zjm 
@Version : 1.0
@Contact : 1005564803@qq.com
@WebSite : https://github.com/sum-123/Python-.git
'''

# here put the import lib
def Countmax(n):
    dic={}
    sum=0
    m=0
    for i in n:
        if i in dic:
          dic[i]+=1
        else:
          dic[i]=1 
    for j in dic:
        if dic[j]>sum:
            sum=dic[j]
            m=j  
    print(m,':',sum) 
str="aaaaabbc"
Countmax(str)
