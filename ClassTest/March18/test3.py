# -*- encoding: utf-8 -*-
'''
@File : test3.py
@Time : 2020/03/19 17:14:14
@Author : zjm 
@Version : 3.7.6
@Contact : 1005564803@qq.com
@WebSite : https://github.com/sum-123/Python-.git
'''

# here put the import lib
import os
f=open('./ClassTest/March18/b_file/zuoye1.txt',encoding='UTF-8')
print(f.read())
f.close()
f=open('./ClassTest/March18/b_file/zuoye1.txt',encoding='gbk')#gbk读取出现乱码
print(f.read())
f.close()
