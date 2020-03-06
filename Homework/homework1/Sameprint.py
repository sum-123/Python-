# -*- encoding: utf-8 -*-
'''
@File : Sameprint.py
@Time : 2020/03/06 12:04:19
@Author : zjm 
@Version : 1.0
@Contact : 1005564803@qq.com
@WebSite : https://github.com/sum-123/Python-.git
'''

# here put the import lib
list1=[1,2,3,4,5,6,7,8,9]
list2=[2,5,7,9]
list3=[]
for x in list1:
    for y in list2:
      if(x==y):
       list3.append(x)
print(list3)
