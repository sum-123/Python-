# -*- encoding: utf-8 -*-
'''
@File : dog.py
@Time : 2020/04/25 14:40:40
@Author : zjm 
@Version : 3.7.6
@Contact : 1005564803@qq.com
@WebSite : https://github.com/sum-123/Python-.git
'''

# here put the import lib
class dog:
    def __init__(self):
        self.blood = 80
        self.attack=15
        self.life=True
    def bit(self,person):
        if self.blood>0:
            person.blood -= self.attack
            print('狗(攻击力{})咬人，人血量{}'.format(self.attack,person.blood))
        else:
            self.life=False
