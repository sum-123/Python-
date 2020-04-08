# -*- encoding: utf-8 -*-
'''
@File : JDtest.py
@Time : 2020/04/08 17:01:37
@Author : zjm 
@Version : 3.7.6
@Contact : 1005564803@qq.com
@WebSite : https://github.com/sum-123/Python-.git
'''

# here put the import lib
import random
def createip(filename):
    ip=['172.25.254.'+str(i) for i in range(1,255)]
    # print(ip)
    with open(filename,'a+') as f:
        for item in range(1200):
            print(random.sample(ip,1))
            f.write(random.sample(ip,1)[0]+'\n')
def sortedip(filename,count=10):
      with open(filename) as f:
          dic=dict()
          for line in f.readlines():
              line=line.strip('\n')
              if line in dic:
                dic[line]+=1
              else:
                dic[line]=1
          dicsort=sorted(dic.items(),key=lambda x:x[1],reverse=True)[:10]
          for i,j in dicsort:
              print(i,'出现的次数为',j)
        #   print(dicsort)
# createip('ip.txt')
sortedip('ip.txt')






