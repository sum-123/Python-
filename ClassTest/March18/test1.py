# -*- encoding: utf-8 -*-
'''
@File : test.py
@Time : 2020/03/18 08:10:34
@Author : zjm 
@Version : 1.0
@Contact : 1005564803@qq.com
@WebSite : https://github.com/sum-123/Python-.git
'''

# here put the import lib
# import os
# print(os.path.dirname('/Users/zhaojiaming/Documents/GitHub/Python-/ClassTest/March18/test.py'))
# print(os.path.split('/Users/zhaojiaming/Documents/GitHub/Python-/ClassTest/March18/test.py'))
# print(os.path.join('Users','March18','test.py'))
# from datetime import datetime
# import os

# pwd = os.path.abspath('.')

# print('      Size     Last Modified  Name')
# print('------------------------------------------------------------')

# for f in os.listdir(pwd):
#     fsize = os.path.getsize(f)
#     mtime = datetime.fromtimestamp(os.path.getmtime(f)).strftime('%Y-%m-%d %H:%M')
#     flag = '/' if os.path.isdir(f) else ''
#     print('%10d  %s  %s%s' % (fsize, mtime, f, flag))
#    MacOS下  os.path使用
import os 
import time
file='/Users/zhaojiaming/Downloads/123.txt'
print( os.path.basename(file) )   # 返回文件名
print( os.path.dirname(file) )    # 返回目录路径
print( os.path.split(file) )      # 分割文件名与路径
print( os.path.join('Users','zhaojiaming','Dowmloads','123.txt') )  # 将目录和文件名合成一个路径
print( os.path.getatime(file) )   # 输出最近访问时间
print( os.path.getctime(file) )   # 输出文件创建时间
print( os.path.getmtime(file) )   # 输出最近修改时间
print( time.gmtime(os.path.getmtime(file)) )  # 以struct_time形式输出最近修改时间
print( os.path.getsize(file) )   # 输出文件大小（字节为单位）
print( os.path.abspath(file) )   # 输出绝对路径
print( os.path.normpath(file) )  # 规范path字符串形式