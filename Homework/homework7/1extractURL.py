# -*- encoding: utf-8 -*-
'''
@File : extractURL.py
@Time : 2020/04/18 15:26:51
@Author : zjm 
@Version : 3.7.6
@Contact : 1005564803@qq.com
@WebSite : https://github.com/sum-123/Python-.git
'''

# here put the import lib
import re

def func(path,path2):
	with open(path,'r',encoding='utf-8')as f:
		res=f.read()
    # print(res)
	obj=re.findall(r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+',res)
    
	with open(path2, 'w', encoding='utf-8')as f2:
		for i in obj:

			f2.write(i+'\n')


if __name__ == '__main__':
	path=r'webspiderUrl.txt'
	path2=r'URL.txt'
	func(path,path2)

