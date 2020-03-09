# -*- encoding: utf-8 -*-
'''
@File : Check_dic.py
@Time : 2020/03/09 18:02:28
@Author : zjm 
@Version : 1.0
@Contact : 1005564803@qq.com
@WebSite : https://github.com/sum-123/Python-.git
'''

# here put the import lib
def fun1(n):
    for i,m in n.items():
        m = str(m)
        if len(m) > 2:
            n[i] = m[0:2]
    print(n)
dic = {'name':'abcdefg','age':2000,'sex':'boyyyyyyy'}
fun1(dic)
