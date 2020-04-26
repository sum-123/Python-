# -*- encoding: utf-8 -*-
'''
@File : people.py
@Time : 2020/04/25 14:40:44
@Author : zjm 
@Version : 3.7.6
@Contact : 1005564803@qq.com
@WebSite : https://github.com/sum-123/Python-.git
'''

# here put the import lib
class people:
    def __init__(self):
        self.blood=100
        self.attack=10
        self.life = True
    def hit(self,dog):
        if self.blood > 0:
            dog.blood -= self.attack
            print('人(攻击力{})打狗，狗血量{}'.format(self.attack,dog.blood))
        else:
            self.life = False 

