# -*- encoding: utf-8 -*-
'''
@File : dog.py
@Time : 2020/04/20 17:36:30
@Author : zjm 
@Version : 3.7.6
@Contact : 1005564803@qq.com
@WebSite : https://github.com/sum-123/Python-.git
'''

# here put the import lib
class dog:
    dog_list  = [{'color': 'blue', 'number': 66, 'price': 300},
                 {'color': 'white', 'number': 88, 'price': 100},
                 {'color': 'green', 'number': 99, 'price': 200}]
    
    def dog_buy(self, color, number):
        for i in range(len(self.dog_list)):
            if self.dog_list[i]['color'] == color:
                self.dog_list[i]['number'] += number
    def dog_sell(self, color, number):
        for i in range(len(self.dog_list)):
            if self.dog_list[i]['color'] == color:
                self.dog_list[i]['number'] -= number
    def print_dog(self):
        for item in self.dog_list:
            print(item['color'], item['number'], item['price'])
dog1=dog()
dog1.dog_sell('blue',20)
dog1.print_dog()
        



