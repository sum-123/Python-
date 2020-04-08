# -*- encoding: utf-8 -*-
'''
@File : TimeComp.py
@Time : 2020/04/02 10:34:57
@Author : zjm 
@Version : 3.7.6
@Contact : 1005564803@qq.com
@WebSite : https://github.com/sum-123/Python-.git
'''

# here put the import lib
import time
from collections import deque
from random import randint
li=[randint(-200,200) for _ in range(10)]
start1=time.time()
li.insert(0,10)
end1=time.time()
li.pop(0)
d=deque(li)
start2=time.time()
d.appendleft(10)
end2=time.time()
print('insert用时%e'%(end1-start1))
print('appendleft用时%e'%(end2-start2))

