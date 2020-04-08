# -*- encoding: utf-8 -*-
'''
@File : SaveUser.py
@Time : 2020/04/02 13:12:56
@Author : zjm 
@Version : 3.7.6
@Contact : 1005564803@qq.com
@WebSite : https://github.com/sum-123/Python-.git
'''

# here put the import lib
import hashlib
def get_md5(data):
    obj = hashlib.md5("12:;idrsicxwersdfsaersdfsdfresdy54436jgfdsjdxff123ad".encode('utf-8'))
    obj.update(data.encode('utf-8'))
    result = obj.hexdigest()
    return result
def register():
    print('**************创建用户**************')
    while True:
        uname = input('请输入姓名:')
        if uname == 'N':
            return
        user = input('请输入账号:')
        pwd = input('请输入密码:')
        temp = {'name':uname,'username':user,'password':get_md5(pwd)}
        with open('user.txt','a') as f:
             f.write(str(temp))
             f.write('\n')
register()
