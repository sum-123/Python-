# -*- encoding: utf-8 -*-
'''
@File : UserLog.py
@Time : 2020/04/02 16:36:02
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
USER_LIST=[]
with open('user.txt','r') as f:
    for line in f.readlines():
       line=line.strip('\n')
       USER_LIST.append(eval(line))

def login():
    print('**************用户登陆**************')
    uname=input('请输入姓名')
    user = input('请输入账号:')
    pwd = input('请输入密码:')

    for item in USER_LIST:
        if item['name']==uname and item['username'] == user and item['password'] == get_md5(pwd):
            return True
# print(USER_LIST)
result = login()
if result:
    print('登陆成功')
else:
    print('登陆失败')