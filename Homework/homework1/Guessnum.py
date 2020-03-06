# -*- encoding: utf-8 -*-
'''
@File : Guessnum.py
@Time : 2020/03/06 13:55:49
@Author : zjm 
@Version : 1.0
@Contact : 1005564803@qq.com
@WebSite : https://github.com/sum-123/Python-.git
'''

# here put the import lib
import random
number=random.randint(1,20)
guess = -1
print("数字猜谜游戏!(数字在为1-20的任意数字)")
while guess != number:
    guess = int(input("请输入你猜的数字："))
 
    if guess == number:
        print("恭喜，你猜对了！")
    elif guess < number:
        print("猜的数字小了...")
    elif guess > number:
        print("猜的数字大了...")