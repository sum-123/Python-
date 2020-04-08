# -*- encoding: utf-8 -*-
'''
@File : SumFile.py
@Time : 2020/04/08 16:43:39
@Author : zjm 
@Version : 3.7.6
@Contact : 1005564803@qq.com
@WebSite : https://github.com/sum-123/Python-.git
'''

# here put the import lib
import os
def Search(path):
    files=os.listdir(path)
    for file in files:
        filepath=path+"/"+file
        if os.path.isdir(filepath):
            Search(filepath)
        else:
            flist.append(filepath)
def Count(flist):
    size=sum([os.path.getsize(file) for file in flist])/1024/1024
    print('文件总大小为:%.2f'%size,'MB')
flist=[]
path='/Users/zhaojiaming/Documents'
Search(path)
Count(flist)