# -*- encoding: utf-8 -*-
'''
@File : test4.py
@Time : 2020/03/06 09:33:17
@Author : zjm 
@Version : 1.0
@Contact : 1005564803@qq.com
@WebSite : https://github.com/sum-123/Python-.git
'''

# here put the import lib
def show(name,age,*arge,**kwargs):
	print(name,age,args,kwargs)
show('zs',20,1,2,3,a='zs',b =10)

