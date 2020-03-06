# -*- encoding: utf-8 -*-
'''
@File : Judgeyear.py
@Time : 2020/03/06 12:10:39
@Author : zjm 
@Version : 1.0
@Contact : 1005564803@qq.com
@WebSite : https://github.com/sum-123/Python-.git
'''

# here put the import lib
x=int(input("请输入需要判断的年份"))
if((x%100!=0 and x%4==0) or x%400==0):
    print(x,'是闰年')
else:
    print(x,'不是闰年')
     