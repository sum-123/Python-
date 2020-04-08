# -*- encoding: utf-8 -*-
'''
@File : DirectOption.py
@Time : 2020/03/31 11:30:27
@Author : zjm 
@Version : 3.7.6
@Contact : 1005564803@qq.com
@WebSite : https://github.com/sum-123/Python-.git
'''

# here put the import lib
import random
import string
import os
from os.path import splitext

def gen_code(len=4):
    list = random.sample(string.ascii_letters+string.digits,len)
    return ''.join(list)

def create_files():
    #随机生成100个验证码
    list = [gen_code() for i in range(10)]
    os.mkdir('img')
    for i in list:
        f = open('./img/%s'%i + '.png',"a")
        f.close()
create_files()
def function(dname,osuffix,nsuffix):
    pngfile=filter(lambda filename:filename.endswith(osuffix),os.listdir(dname))
    mainfiles=[os.path.splitext(filename)[0] for filename in pngfile]
    for filename in mainfiles:
        oname=os.path.join(dname,filename+osuffix)
        nname=os.path.join(dname,filename+nsuffix)
        os.rename(oname,nname)
function('img','.png','.jpg')
