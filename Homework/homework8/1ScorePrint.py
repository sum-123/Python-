# -*- encoding: utf-8 -*-
'''
@File : ScorePrint.py
@Time : 2020/05/01 09:35:04
@Author : zjm 
@Version : 3.7.6
@Contact : 1005564803@qq.com
@WebSite : https://github.com/sum-123/Python-.git
'''

# here put the import lib
from random import randint
import random
from multiprocessing import Pool
import threading
lis=[randint(60,100) for _ in range(100)]
# **********多线程实现**********
def Mutiprint(lis):
    for i in  range(0,100):
        print('第%d个学生成绩%d'%(i+1,lis[i]))

res = list(range(10))

for i in  range(5):
    threading.Thread(target=Mutiprint,args=(res[i*20:(i+1)*20],))

Mutiprint(lis)
# ***********进程池实现**********
# num=0
# def printLis():
#    global num
#    global lis
#    print('第%d个学生成绩%d'%(num+1,lis[num]))
#    num+=1

# pool = Pool(5)
# for i in range(0,100):
#     pool.apply_async(printLis)

# pool.close()
# pool.join()

