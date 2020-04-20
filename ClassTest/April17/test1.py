# -*- encoding: utf-8 -*-
'''
@File : test1.py
@Time : 2020/04/17 07:47:31
@Author : zjm 
@Version : 3.7.6
@Contact : 1005564803@qq.com
@WebSite : https://github.com/sum-123/Python-.git
'''

# here put the import lib
# import time
# import threading

# def sing():
#     """ 唱歌5秒钟"""
#     for i in range(5):
#             print("****正在唱歌****")
#             time.sleep(1)

# def dance():
#     """ 唱歌5秒钟"""
#     for i in range(5):
#             print("*****正在跳舞*******")
#             time.sleep(1)

# def main():
#         t1=threading.Thread(target=sing)
#         t2=threading.Thread(target=dance)
#         t1.start()
#         t2.start()
# main()
# import time

# def saySorry():
#     print("亲爱的，我错了，我能吃饭了吗？")
#     time.sleep(1)

# if __name__ == "__main__":
#     for i in range(5):
#         saySorry()
# import threading
# import time

# def saySorry():
#     print("亲爱的，我错了，我能吃饭了吗？")
#     time.sleep(2)

# if __name__ == "__main__":
#     for i in range(5):
#         t = threading.Thread(target=saySorry)
#         t.start() #启动线程，即让线程开始执行
# import threading
# from time import sleep,ctime

# def sing():
#     for i in range(3):
#         print("正在唱歌...%d"%i)
#         sleep(1)

# def dance():
#     for i in range(3):
#         print("正在跳舞...%d"%i)
#         sleep(1)

# if __name__ == '__main__':
#     print('---开始---:%s'%ctime())

#     t1 = threading.Thread(target=sing)
#     t2 = threading.Thread(target=dance)

#     t1.start()
#     t2.start()

#     sleep(2) # 屏蔽此行代码，试试看，程序是否会立马结束？
#     print('---结束---:%s'%ctime())
# import threading
# from time import sleep,ctime

# def sing():
#     for i in range(3):
#         print("正在唱歌...%d"%i)
#         sleep(1)

# def dance():
#     for i in range(3):
#         print("正在跳舞...%d"%i)
#         sleep(1)

# if __name__ == '__main__':
#     print('---开始---:%s'%ctime())

#     t1 = threading.Thread(target=sing)
#     t2 = threading.Thread(target=dance)

#     t1.start()
#     t2.start()

#     while True:
#         length = len(threading.enumerate())
#         print('当前运行的线程数为：%d'%length)
#         if length<=1:
#             break

#         sleep(0.5)
# class people:
#     #定义基本属性
#     name = ''
#     age = 0
#     #定义私有属性,私有属性在类外部无法直接进行访问
#     __weight = 0
#     #定义构造方法
#     def __init__(self,n,a,w):
#         self.name = n
#         self.age = a
#         self.__weight = w
#     def speak(self):
#         print("%s 说: 我 %d 岁。" %(self.name,self.age))
 
# # 实例化类
# p = people('runoob',10,30)
# p.speak()
# 类定义
# class people:
#     #定义基本属性
#     name = ''
#     age = 0
#     #定义私有属性,私有属性在类外部无法直接进行访问
#     __weight = 0
#     #定义构造方法
#     def __init__(self,n,a,w):
#         self.name = n
#         self.age = a
#         self.__weight = w
#     def speak(self):
#         print("%s 说: 我 %d 岁。" %(self.name,self.age))
 
# #单继承示例
# class student(people):
#     grade = ''
#     def __init__(self,n,a,w,g):
#         #调用父类的构函
#         people.__init__(self,n,a,w)
#         self.grade = g
#     #覆写父类的方法
#     def speak(self):
#         print("%s 说: 我 %d 岁了，我在读 %d 年级"%(self.name,self.age,self.grade))
 
# # 另一个类，多重继承之前的准备
# class speaker():
#     topic = ''
#     name = ''
#     def __init__(self,n,t):
#         self.name = n
#         self.topic = t
#     def speak(self):
#         print("我叫 %s，我是一个演说家，我演讲的主题是 %s"%(self.name,self.topic))
 
# #多重继承
# class sample(speaker,student):
#     a =''
#     def __init__(self,n,a,w,g,t):
#         student.__init__(self,n,a,w,g)
#         speaker.__init__(self,n,t)
 
# test = sample("Tim",25,80,4,"Python")
# test.speak()   #方法名同，默认调用的是在括号中排前地父类的方法
# class parent:
#     def mymethod(self):
#         print('父类方法')
# class child(parent):
#     def mymethod(self):
#         print('子类方法')
# a=child()
# a.mymethod()
# super(child,a).mymethod()
# class Vector:
#    def __init__(self, a, b):
#       self.a = a
#       self.b = b
 
#    def __str__(self):
#       return 'Vector (%d, %d)' % (self.a, self.b)
   
#    def __add__(self,other):
#       return Vector(self.a + other.a, self.b + other.b)
# v1 = Vector(2,10)
# v2 = Vector(5,-2)
# print (v1 + v2)
# import sys
# sys.path.append('/Users/zhaojiaming/Documents/GitHub/Python-')
# from ClassTest.April17.test2 import Person
# obj=Person()
# print(obj.method())
# print(obj.__module__)  # 输出 test 即：输出模块
# print(obj.__class__)  # 输出 test.Person 即：输出类
# class Dog:
#     def __init__(self,age):
#         if age>10 and age<100:
#             self.age=age
#         else:
#             self.age=0
#     def getage(self):
#         return self.age
# dog1=Dog(100)
# print(dog1.getage())
class cat:
    def eat(self):
        print(' cat eat fish') 
    def drink(self):
        print('cat drink water')
    def introduce(self):
        print('%s age is : %d'%(tom.name,tom.age))
tom=cat()
tom.eat()
tom.drink()
tom.name='Tom'
tom.age=10
tom.introduce()
      
          
