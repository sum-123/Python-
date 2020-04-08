# -*- encoding: utf-8 -*-
'''
@File : Textoption.py
@Time : 2020/03/06 14:48:45
@Author : zjm 
@Version : 1.0
@Contact : 1005564803@qq.com
@WebSite : https://github.com/sum-123/Python-.git
'''

# here put the import lib
import operator
word="I'm a boby, I'm a girl. When it is true, it is ture. thit are cats, the red is red,the red is red,the red is red,the red is red."
word=word.replace(',','').replace('.','')
word=word.split()
dic={}
print(word)
for k in word:
    if k in dic:
        dic[k]+=1
    else:
        dic[k]=1
#print(dic)
a1 = sorted(dic.items(),key = lambda x:x[1],reverse = True)
#print(a1)
for i,j in a1:
    print(i,'出现的次数为',j)

