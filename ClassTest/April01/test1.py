# -*- encoding: utf-8 -*-
'''
@File : test1.py
@Time : 2020/04/01 08:22:23
@Author : zjm 
@Version : 3.7.6
@Contact : 1005564803@qq.com
@WebSite : https://github.com/sum-123/Python-.git
'''

# here put the import lib
import time
# def foo():
#     time.sleep(2)
#     print("from the foo")

# def test(func):
#     return func

# foo=test(foo)
# start=time.time()
# foo()
# end=time.time()
# print("执行时间%s"%(end-start))


# def foo():
#     time.sleep(3)
#     print("来自foo")

# #不修改foo源代码
# #不修改foo调用方式

# def timer(func):
#     start=time.time()
#     func()
#     end=time.time()
#     print("执行时间%s"%(end-start))
#     return func
# f=timer(foo)
# f()
# def jia(x,y):
#     return x+y;
# def jisuan(x,y,add):
#     return add
# a=jisuan(1,2,jia)

# def square(x):    
#     return x**2
# list1=[1,3,5,7] 
# res=map(square,list1) 
# print(list(res)) 
#匿名函数的写法 
# print(list(map(lambda x: x ** 2, [1, 2, 3, 4, 5])))
from functools import reduce
# def add(x,y): 
#     return x+y 
# print(reduce(add,[1,2,3,4,5]))  
# print(reduce(lambda x,y:x*y,[1,2,3,4,5]))

# list1=[1,2,3,4,5,6,7,8,9,10] 
# def even(x):
#      return x%2!=1 
# print(list(filter(even,list1)))
# print(list(filter(lambda x:x%2==0,[1,2,3,4,5,6,7,8,9,10])))
# l=range(10)
# print(list(l))
# print(list(filter(lambda x:x%2==0,l)))
# def lazy_sum(*args):
#     def sum():
#         ax = 0
#         for n in args:
#             ax = ax + n
#         return ax
#     return sum
# a=lazy_sum(1,3,5,7,9)
# print(a())
import json
li=[]
f= open('user.txt','r')
for line in f.readlines():
    line=line.strip('\n')
    li.append(eval(line))

   

    
f.close()
print(li)