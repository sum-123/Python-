# -*- encoding: utf-8 -*-
'''
@File : Listfile.py
@Time : 2020/04/02 17:22:43
@Author : zjm 
@Version : 3.7.6
@Contact : 1005564803@qq.com
@WebSite : https://github.com/sum-123/Python-.git
'''

# here put the import lib
import os
import time
import datetime
def istype(file):
    if os.path.isdir (file):
        return '文件夹'
    else:
        return '文件'


def get_time(timestamp):
    return datetime.datetime.fromtimestamp(timestamp)
files = os.listdir('/Users/zhaojiaming/Documents/Github/Python-')
print('名称',' '*30,'创建时间',' '*8,'大小',' '*8,'类型')
for file in files:
    fileinto=os.path.getctime(file)
    filesize=os.path.getsize(file)
    print(file,'                     ',get_time(fileinto).replace(microsecond=0),filesize/1024,'KB','       ',istype(file))
	


