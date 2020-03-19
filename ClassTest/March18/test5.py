# -*- encoding: utf-8 -*-
'''
@File : test5.py
@Time : 2020/03/19 18:51:30
@Author : zjm 
@Version : 3.7.6
@Contact : 1005564803@qq.com
@WebSite : https://github.com/sum-123/Python-.git
'''

# here put the import lib
import pickle
obj = {
        "Jack": 18, 
        "Bis": 20, 
        "Sam":19
      }
f = open("./ClassTest/March18/b_file/test5.txt","wb")
pickle.dump(obj, f)
del obj
f.close()

f2 = open("./ClassTest/March18/b_file/test5.txt","rb")
# 从 tmp.txt 中读取并恢复 obj 对象
obj2 = pickle.load(f2)
f2.close()

print(obj2)