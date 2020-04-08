# -*- encoding: utf-8 -*-
'''
@File : Imagdownload.py
@Time : 2020/04/08 20:33:52
@Author : zjm 
@Version : 3.7.6
@Contact : 1005564803@qq.com
@WebSite : https://github.com/sum-123/Python-.git
'''

# here put the import lib
import requests
import os
url="http://www.biyunet.com/upimages/201451316405.jpg"
dir_path='/Users/zhaojiaming/Downloads/'
path=dir_path+url.split('/')[-1]
try:
    if not os.path.exists(path):
        x=requests.get(url)
        x.raise_for_status()
        with open(path,'wb') as f:
            f.write(x.content)
            print('图片已保存')
    else:
        print('图片已存在')
except:
    print('图片下载失败')



