# -*- encoding: utf-8 -*-
'''
@File : Logging.py
@Time : 2020/04/13 21:24:06
@Author : zjm 
@Version : 3.7.6
@Contact : 1005564803@qq.com
@WebSite : https://github.com/sum-123/Python-.git
'''

# here put the import lib
import time
def add_log_wrapper(func):
    def inner(*args, **kwargs):
        with open('log.txt', 'a', encoding='utf-8') as f:
            now_time = time.strftime('%Y-%m-%d %X')
            func_name = func.__name__
            log_str = f'{now_time} {func_name} 运行\n'
            print(log_str)
            f.write(log_str)
        res = func(*args, **kwargs)  
        return res
    return inner

@add_log_wrapper
def f1():
    time.sleep(3)
    print('f1函数的执行...')
f1()




