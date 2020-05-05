# -*- encoding: utf-8 -*-
'''
@File : primePrint.py
@Time : 2020/05/01 10:16:29
@Author : zjm 
@Version : 3.7.6
@Contact : 1005564803@qq.com
@WebSite : https://github.com/sum-123/Python-.git
'''

# here put the import lib
import time
import math
import multiprocessing
from concurrent.futures import  ThreadPoolExecutor

def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def pool(count):
    pool = multiprocessing.Pool(count)

    lis = []
    start_time = time.time()
    for i in range(1,100000):
        if pool.apply(isPrime,args=(i,))==True:
            lis.append(i)
    pool.close()

    pool.join()

    print('成功运行,result = %d' %(len(lis)))
    print('运行时间为:%s' %(time.time() - start_time))
pool(10)
pool(4)

