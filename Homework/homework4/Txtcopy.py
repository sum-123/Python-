# -*- encoding: utf-8 -*-
'''
@File : Txtcopy.py
@Time : 2020/04/02 17:09:07
@Author : zjm 
@Version : 3.7.6
@Contact : 1005564803@qq.com
@WebSite : https://github.com/sum-123/Python-.git
'''

# here put the import lib
import os
import shutil
source_path = os.path.abspath(r'/Users/zhaojiaming/Documents/Github/Python-/copy1.txt')
target_path = os.path.abspath(r'/Users/zhaojiaming/Documents/Github/Python-/copy2.txt')
shutil.copy(source_path,target_path)