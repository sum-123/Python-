# -*- encoding: utf-8 -*-
'''
@File : Studentclass2.py
@Time : 2020/04/20 17:02:25
@Author : zjm 
@Version : 3.7.6
@Contact : 1005564803@qq.com
@WebSite : https://github.com/sum-123/Python-.git
'''

# here put the import lib
class Student:
    def __init__(self,name,age,sex,English,Math,Chinese):
        self.name=name
        self.age=age
        self.sex=sex
        self.English=English
        self.Math=Math
        self.Chinese=Chinese
    def sumScore(self):
        return self.English+self.Math+self.Chinese
    def averageScore(self):
        return (self.English+self.Math+self.Chinese)/3
stu1=Student('Jack','18','男',98,99,97)
print('学生姓名为',stu1.name,'总分为',stu1.sumScore(),'平均分为',stu1.averageScore())

