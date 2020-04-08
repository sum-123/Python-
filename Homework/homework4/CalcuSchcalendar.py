# -*- encoding: utf-8 -*-
'''
@File : CalcuSchcalendar.py
@Time : 2020/04/02 10:58:03
@Author : zjm 
@Version : 3.7.6
@Contact : 1005564803@qq.com
@WebSite : https://github.com/sum-123/Python-.git
'''

# here put the import lib

import time
from datetime import datetime
def CalSchcalendar():
    str=input('请输入一个日期（包含年月日）')
    week = datetime.strptime("2020217","%Y%m%d").strftime("%W")
    week1 = datetime.strptime(str,"%Y%m%d").strftime("%W")
    a=int(week1)-int(week)+1
    print('当前是校历第%d周'%(a))
CalSchcalendar()
