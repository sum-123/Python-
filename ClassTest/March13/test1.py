# -*- encoding: utf-8 -*-
'''
@File : test1.py
@Time : 2020/03/13 08:10:26
@Author : zjm 
@Version : 1.0
@Contact : 1005564803@qq.com
@WebSite : https://github.com/sum-123/Python-.git
'''

# here put the import lib
# from collections import Counter
# from random import randint
# list1=[randint(0,100) for _ in range(20)]
# print(list1)
# list1.sort()
# print(list1)
# list1.reverse()
# print(list1)
# list2=sorted(list1)
# print(list1)
# print(list2)
# sentence = "I can because i think i can"
# list3=sentence.split()
# print(list3)
# print(sentence)
# set1=set(list3)
# result={word:list3.count(word) for word in set1}
# print(result)
# result = {word: sentence.split().count(word) for word in set(sentence.split())}
# print(result)
# counts=Counter(list3)
# print(counts)
s = ' das1 32 a2da'
def lei(l):
    num = 0
    isah = 0
    kong = 0
    other = 0
    for i in l :
        if i.isdigit():
            num +=1
        elif i.isalpha():
            isah +=1
        elif i.isspace():
             kong +=1
        else:
             other +=1
    return num,isah,kong,other

print(lei(s))
