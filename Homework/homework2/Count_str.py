# -*- encoding: utf-8 -*-
'''
@File : Count_str.py
@Time : 2020/03/09 17:36:39
@Author : zjm 
@Version : 1.0
@Contact : 1005564803@qq.com
@WebSite : https://github.com/sum-123/Python-.git
'''

# here put the import lib
def count_str(n):
    count1=0
    count2=0
    count3=0
    count4=0
    for i in n:
        if i.isdigit()==True:
            count1+=1
        elif i.isalpha()==True:
            count2+=1
        elif i.isspace()==True:
            count3+=1
        else:
            count4+=1
    print("数字有%d个"%count1)
    print("字母有%d个"%count2)
    print("空格有%d个"%count3)
    print("其它有%d个"%count4)
str="abc,,sd,  ,s，12123132432"
count_str(str)
        

