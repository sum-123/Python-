# -*- encoding: utf-8 -*-
'''
@File : test4.py
@Time : 2020/03/19 17:23:05
@Author : zjm 
@Version : 3.7.6
@Contact : 1005564803@qq.com
@WebSite : https://github.com/sum-123/Python-.git
'''

# here put the import lib
import os
# f=open('./ClassTest/March18/b_file/zuoye1.txt',encoding='UTF-8')
# for line in f.readlines():
#     print(line)

with open('./ClassTest/March18/b_file/zuoye1.txt', 'r') as f:
    line=f.readline()
    line1=f.readline()
    line2=f.readline()
    line3=f.readline()
print(line,end='') 
print(line2,end='')
print(line3)
print(line1)
with open('./ClassTest/March18/b_file/test4.txt', 'w') as f:
    f.write(line)
    f.write(line2)
    f.write(line3)
    f.write(line1)
    f.close()

