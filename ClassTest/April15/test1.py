# -*- encoding: utf-8 -*-
'''
@File : test1.py
@Time : 2020/04/15 08:11:40
@Author : zjm 
@Version : 3.7.6
@Contact : 1005564803@qq.com
@WebSite : https://github.com/sum-123/Python-.git
'''

# here put the import lib
import re
text=input('输入邮箱地址')
ret=re.match(r'^[0-9a-zA-Z_]{4,20}@163\.com$',text)
print(ret.group())

