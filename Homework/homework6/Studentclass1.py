# -*- encoding: utf-8 -*-
'''
@File : Studentclass.py
@Time : 2020/04/15 21:33:50
@Author : zjm 
@Version : 3.7.6
@Contact : 1005564803@qq.com
@WebSite : https://github.com/sum-123/Python-.git
'''

# here put the import lib
class Student:
    def __init__(self,name,age,score):
        self.name=name
        self.age=age
        self.score=score
    def get_name(self):
        if isinstance(self.name,str):
            return self.name
    def get_age(self):
        if isinstance(self.age,int):
            return self.age
    def get_score(self):
        m = max(self.score)
        if isinstance(m, int):
            return m
student1=Student('Jack',18,[98,99,97])
print(student1.get_name())
print(student1.get_age())
print(student1.get_score())
student2=Student('Tom',19,[88,77,95])
print(student2.get_name())
print(student2.get_age())
print(student2.get_score())


    

        
