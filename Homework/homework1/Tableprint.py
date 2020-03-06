# -*- encoding: utf-8 -*-
'''
@File : Tableprint.py
@Time : 2020/03/06 13:26:16
@Author : zjm 
@Version : 1.0
@Contact : 1005564803@qq.com
@WebSite : https://github.com/sum-123/Python-.git
'''

# here put the import lib

for  i in range(1,10):
    for j in range(1,10):
        if(i>=j):
         print('%d*%d=%d'%(j,i,i*j),end='   ')
    print('\n')
