# -*- encoding: utf-8 -*-
'''
@File : Elemprint.py
@Time : 2020/03/06 10:37:48
@Author : zjm 
@Version : 1.0
@Contact : 1005564803@qq.com
@WebSite : https://github.com/sum-123/Python-.git
'''

# here put the import lib
list1=[]
for i in range(1,51):
    if i%2==0:
      list1.append(i)
print(list1)
list2=[]
for i in range(1,51):
    if i%2!=0:
      list2.append(i)
print(list2) 
list3=[]
for i in range(1,51):
    if i%2==0 and i%3==0:
       list3.append(i)
print(list3)
