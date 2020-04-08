# -*- encoding: utf-8 -*-
'''
@File : Readtxt.py
@Time : 2020/03/26 19:31:14
@Author : zjm 
@Version : 3.7.6
@Contact : 1005564803@qq.com
@WebSite : https://github.com/sum-123/Python-.git
'''
#here put the import lib

def input_List():
    List=[]
    while True:
        t=input('');
        if not t:
            return List
        List.append(t)
def txt_f(List):
    try:
        f=open('/Users/zhaojiaming/Documents/GitHub/Python-/Homework/homework3/input.txt','w')
        for s in List:
            f.write(s)
            f.write('\n')
        f.close()
    except IOError:
        print("写入失败")
txt_f(input_List())   
