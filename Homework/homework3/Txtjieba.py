# -*- encoding: utf-8 -*-
'''
@File : Txtjieba.py
@Time : 2020/03/31 16:07:08
@Author : zjm 
@Version : 3.7.6
@Contact : 1005564803@qq.com
@WebSite : https://github.com/sum-123/Python-.git
'''

# here put the import lib
import jieba  
def Handle():
    txt = open("ChineseTxt.txt", encoding="UTF-8").read()  
    txt.lower()
    for ch in "“，。、”":
        txt=txt.replace(ch, "")
    return txt
txt=Handle()
words  = jieba.lcut(txt)  
counts = {}  
for word in words:  
    counts[word] = counts.get(word,0) + 1  
items = list(counts.items())  
items.sort(key=lambda x:x[1], reverse=True)   
for i in range(30):  
    word, count = items[i]  
    print ("{0:<10}{1:>5}".format(word, count))


