# -*- encoding: utf-8 -*-
'''
@File : SelectStu.py
@Time : 2020/03/06 11:29:43
@Author : zjm 
@Version : 1.0
@Contact : 1005564803@qq.com
@WebSite : https://github.com/sum-123/Python-.git
'''

# here put the import lib
STU={10001:89,10002:85,10003:98,10004:97,10005:99,10006:76,10007:67,10008:63,10009:59,10010:60}
for key,value in STU.items():
    if(value>80):
     print('学号',key,'成绩',value)
   