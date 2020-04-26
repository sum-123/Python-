# -*- encoding: utf-8 -*-
'''
@File : StudentOS.py
@Time : 2020/04/25 17:02:47
@Author : zjm 
@Version : 3.7.6
@Contact : 1005564803@qq.com
@WebSite : https://github.com/sum-123/Python-.git

@descoration : 用面向对象,实现一个学生Python成绩管理系统;
               学生的信息存储在文件中;学生信息的字段有(班级,学号,姓名, Python成绩)
               实现对学生信息及成绩的增,删,改,查方法;
'''

# here put the import lib
import os
class Student:
    def  __init__(self, name, stuClass,id,score):
      self.name = name
      self.stuClass = stuClass
      self.id = id
      self.score = score
    def __str__(self):
        info =  "学生信息：id=" + self.id + ",name=" + self.name + ",stuClass=" + self.stuClass +",Python 分数为"+self.score
        return info
    def getName(self):
        return self.name
    def getId(self):
        return self.id
    def getStuClass(self):
        return self.stuClass
    def getScore(self):
        return self.score
    def setName(self,name):
        self.name=name
    def setStuClass(self):
        self.stuClass=stuClass
    def setScore(self):
        self.score=score
def addStudent(StuList):
    id=input('请输入学生的学号：')
    for i in range(len(StuList)):
        stu1=StuList[i]
        if id == stu1.getId():
            print('学号已存在，不能重复添加')
            return
    name = input('请输入学生姓名')
    stuclass = input('请输入学生班级')
    score = input('请输入Python分数')
    stu=Student(name,stuclass,id,score)
    StuList.append(stu)
    print('学生信息添加成功',stu)
def delStudent(StuList):
    id = input('请输入要删除学生的学号：')
    for i in range(len(StuList)):
        stu1 = StuList[i]
        if id == stu1.getId():
            del StuList[i]

            return 0
    return 1
def updateStudent(StuList):
    id=input('请输入学生的学号：')
    for i in range(len(StuList)):
        stu1 = StuList[i]
        if id == stu1.getId():
            name = input("请输入要修改的学生姓名：")
            stuclass = input("请输入要修改的学生班级：")
            score = input('请输入Python分数')
            stu1.setName(name)
            stu1.setStuClass(stuclass)
            stu1.setScore(score)
            print("修改成功")
            return
    print("找不到该学生学号，无法修改")
def selSutdent(StuList):
    id=input('请输入学生的学号：')
    for i in range(len(StuList)):
        stu1 = StuList[i]
        if id == stu1.getId():
            print('学生信息为',stu1)
            return
    print('查询失败')
    return
def printStuInfo(StuList):
    for i in range(len(StuList)):
        stu = StuList[i]
        print(stu)
print('*'*30)
print('1.添加学生信息')
print('2.删除学生信息')
print('3.修改学生信息')
print('4.查询学生信息')
print('5.退出学生信息管理系统')
print('*'*30)
flag = 0
StuList=[]
filename = 'StuData.txt'
if not os.path.exists(filename):
    file = open(filename,'w')
    file.close()
f = open(filename,'r')
con = f.readlines()
print('文件内容：',con)
StuList.extend(con)
temp=[]
for i in range(len(StuList)):
    print('第'+str(i)+'行:',StuList[i])
    if isinstance(StuList[i],str):
        strArray = str(StuList[i]).split(",")
        name = strArray[0]
        stuclass = strArray[1]
        id = strArray[2]
        score = strArray[3].replace("\n","")
        student = Student(name, stuclass,id,score)
        temp.append(student)
del StuList
StuList = temp 
while flag !=1:
    action = int(input('请选择操作'))
    if action == 1:
        addStudent(StuList)
    elif action == 2:
        n = delStudent(StuList)
        if n == 0:
            print('删除成功')
        elif n==1 or n == 2:
            print('删除失败')
        printStuInfo(StuList)
    elif action == 3:
        updateStudent(StuList)
        printStuInfo(StuList)
    elif action == 4:
        selSutdent(StuList)
    elif action == 5:
        flag == 1
        with open(filename,'w') as f:
            for i in range(len(StuList)):
                if i == len(StuList)-1:
                    stu = StuList[i]
                    f.write(stu.getName()+stu.getStuClass()+stu.getId()+stu.getScore())
                else:
                    stu = StuList[i]
                    f.write(stu.getName()+stu.getStuClass()+stu.getId()+stu.getScore()+'\n')
            f.close()
    else:
        print('输入错误')
print('退出成功')
    







