# -*- encoding: utf-8 -*-
'''
@File : Txt.py
@Time : 2020/03/31 15:26:42
@Author : zjm 
@Version : 3.7.6
@Contact : 1005564803@qq.com
@WebSite : https://github.com/sum-123/Python-.git
'''

# here put the import lib
def HandleTxt():
    txt=open('The Old Man and the Sea.txt','r').read()
    txt=txt.lower()
    for ch in "!'#$%&()*+,-./:'<=>?@[\\]^-‘{|}~":
        txt=txt.replace(ch," ")   
    return txt
ThisTxt=HandleTxt()
words=ThisTxt.split()
dic={}
for word in words:
    dic[word]=dic.get(word,0)+1
list1=list(dic.items())
list1.sort(key=lambda x:x[-1],reverse=True)
for i in range(20):
    word,dic=list1[i]
    print("{0:<20}{1:>5}".format(word,dic))



        