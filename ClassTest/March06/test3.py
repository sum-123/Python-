# -*- encoding: utf-8 -*-
'''
@File : test3.py
@Time : 2020/03/06 09:17:56
@Author : zjm 
@Version : 1.0
@Contact : 1005564803@qq.com
@WebSite : https://github.com/sum-123/Python-.git
'''

# here put the import lib

def printinfo( name, age ):
   "打印任何传入的字符串"
   print ("名字: ", name)
   print ("年龄: ", age)
   return
 
#调用printinfo函数
printinfo( age=50, name="runoob" )
squared = map(lambda x: x**3, [1, 2, 3, 4, 5])
print(list(squared))
a=lambda x:x*x
print(a(4))
list1=[1,2,3,4,5,6,7,8,9]
res=filter(lambda x: x%2==0,list1)
print(list(res))
a=list(range(1,21))
print(a)
rest=filter(lambda x:x%2!=0,a)
print(list(rest))