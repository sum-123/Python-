# -*- encoding: utf-8 -*-
'''
@File : Judge.py
@Time : 2020/05/01 10:42:29
@Author : zjm 
@Version : 3.7.6
@Contact : 1005564803@qq.com
@WebSite : https://github.com/sum-123/Python-.git
'''
# 给定一组数据网址数据，请判断这些网址是否可以访问； 用多线程的方式来实现；
# here put the import lib
import requests
import threading
lis=[]
def getHtmlText(url):
    try:        
        r = requests.get(url,timeout=30)    
        r.raise_for_status()       
        r.encoding = r.apparent_encoding
        return '访问成功'
    except:
         return "访问失败"
def record():
    global lis
    for i in range(len(lis)):
        print(lis[i],getHtmlText(lis[i]))

def ThreadUse():
    for i in range(5):
        t=threading.Thread(target=record)
        t.start()

def main():   
    with open('url_data.txt','r') as f:
        for line in f.readlines():
            a=line.strip('\n')           
            lis.append(a)
    ThreadUse()
    
main()
