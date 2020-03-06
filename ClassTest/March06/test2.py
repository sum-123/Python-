# -*- encoding: utf-8 -*-
'''
@File : test2.py
@Time : 2020/03/06 08:34:53
@Author : zjm 
@Version : 1.0
@Contact : 1005564803@qq.com
@WebSite : https://github.com/sum-123/Python-.git
'''

# here put the import lib
def printList(mylist):
    mylist.append([9,10,11])
    
mylist=[1,2,3,4,5,6,7,8]
print(id(mylist))
printList(mylist)
print(id(mylist))