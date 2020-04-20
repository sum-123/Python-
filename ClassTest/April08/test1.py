# -*- encoding: utf-8 -*-
'''
@File : test2.py
@Time : 2020/04/08 08:17:03
@Author : zjm 
@Version : 3.7.6
@Contact : 1005564803@qq.com
@WebSite : https://github.com/sum-123/Python-.git
'''


# here put the import lib
class Dog:
    count = 0;

    def __init__(self, color, name):
        self.color = color
        self.name = name
        Dog.count += 1

    def shout(self):
        print(self.color + '颜色的' + self.name + '在叫喊')


dog1 = Dog('blue', 'dog1')
dog1.shout()
dog2 = Dog('yellow', 'dog2')
dog2.shout()
print('共有%d' % Dog.count, '只狗')
