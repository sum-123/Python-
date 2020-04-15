# -*- encoding: utf-8 -*-
'''
@File : account.py
@Time : 2020/04/14 15:12:17
@Author : zjm 
@Version : 3.7.6
@Contact : 1005564803@qq.com
@WebSite : https://github.com/sum-123/Python-.git
'''

# here put the import lib
# @Time     :2019/7/2 21:38

'''
编写装饰器，为多个函数加上认证的功能（用户的账号密码来源于文件），
要求登录成功一次，后续的函数都无需再输入用户名和密码
'''
Status = False #用于判断是否已经通过验证

def login(func):
    account_dict = {} #账号密码验证用的，可以换其他方式验证  账号当做key，密码当做value
    def inner():
        global Status

        if not Status :
            with open('account',encoding='utf-8') as f:
                account_data = f.read().split('\n')
                for item in account_data:
                    user, pwd= item.split()
                    account_dict.setdefault(user,pwd)

            username = input("username: ").strip()
            # username = 'da'
            password = input("password: ").strip()
            # password = 'da'
            #验证输入的账号是否在account_dict已存在
            #用.__contains__方法 是为了输入的用户名不存在，然后报 key不存在的错误
            if account_dict.__contains__(username) and account_dict[username] == password:
                Status = True #修改用户登录状态
                print("登陆中~~~".center(50))
                func()#执行传入的函数
            else:
                print('账号密码不匹配')

        else:
            print('已通过验证'.center(50))
            func()

    return inner

@login
def func1():
    print('--func1--')

@login
def func2():
    print('--func2--')

@login
def func3():
    print('--func3--')

func1()
func2()
func3()