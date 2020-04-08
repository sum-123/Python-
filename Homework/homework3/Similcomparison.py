# -*- encoding: utf-8 -*-
'''
@File : Similcomparison.py
@Time : 2020/03/31 20:51:13
@Author : zjm 
@Version : 3.7.6
@Contact : 1005564803@qq.com
@WebSite : https://github.com/sum-123/Python-.git
'''

# here put the import lib
import os
def HandleTxt(file):
    txt=open(file,'r').read()
    txt=txt.lower()
    for ch in "!'#$%&()*+,-./:'<=>?@[\\]^-‘{|}~":
        txt=txt.replace(ch," ")   
    return txt
txt=HandleTxt('python1.txt')
txt1=HandleTxt('python2.txt')
words=txt.split()
words1=txt1.split()
dic={}
for word in words:
    dic[word]=dic.get(word,0)+1
list1=list(dic.items())
list1.sort(key=lambda x:x[-1],reverse=True)
for word1 in words1:
    dic[word1]=dic.get(word1,0)+1
list2=list(dic.items())
list2.sort(key=lambda x:x[-1],reverse=True)
list1=list1[0:10]
list2=list2[0:10]
dic1=dict(list1)
dic2=dict(list2)
# print(list1)
# print(list2)
m=0
for i in dic1:
    for j in dic2:
        if(i==j):
            m=m+1
print('两篇文章的相似度为','%d0'%(m),'%')
# for i in range(20):
#     word,dic=list1[i]
# print("{0:<20}{1:>5}".format(word,dic))
f=open('Towtxt.txt','w')
f.write()


    

