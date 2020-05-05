# -*- encoding: utf-8 -*-
'''
@File : test1.py
@Time : 2020/05/05 21:31:34
@Author : zjm 
@Version : 3.7.6
@Contact : 1005564803@qq.com
@WebSite : https://github.com/sum-123/Python-.git
'''

# here put the import lib
import requests
url='http://www.listeningexpress.com/studioclassroom/ad/sc-ad%202020-05-05%20The%20Faroe%20Islands.mp3'
ret=requests.get(url)
with open('1.mp3','wb') as f:
    f.write(ret.content)
    