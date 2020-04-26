# -*- encoding: utf-8 -*-
'''
@File : dogfight.py
@Time : 2020/04/20 22:46:37
@Author : zjm 
@Version : 3.7.6
@Contact : 1005564803@qq.com
@WebSite : https://github.com/sum-123/Python-.git
'''

# here put the import lib
from dog import dog
from people import people
import random
def main():
    dogs=[]
    peoples=[]
    for i in range(2):
        person=people()
        peoples.append(person)
    for i in range(3):
        dog1=dog()
        dogs.append(dog1)
    # print(random.choice(peoples))
            
    while len(peoples)!= 0 and len(dogs)!=0:
        person = random.choice(peoples)
        if person.life:
            dog1=random.choice(dogs)
            if dog1.life:
                person.hit(dog1)
                dog1.bit(person)
            else:
                dogs.remove(dog1)
        else:
            peoples.remove(person)
    else:
        if len(peoples)!=0:
            print('人赢了')
        else:
            print('狗赢了')
if __name__ == '__main__':
     main()
    

        


