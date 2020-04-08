# -*- encoding: utf-8 -*-
'''
@File : BlowWindy.py
@Time : 2020/03/31 14:40:12
@Author : zjm 
@Version : 3.7.6
@Contact : 1005564803@qq.com
@WebSite : https://github.com/sum-123/Python-.git
'''

# here put the import lib
import os 

# f=open('Blowing in the wind.txt','w')
# f.write('How many roads must a man walk down'+'\n')
# f.write('Before they call him a man'+'\n')
# f.write('How many seas must a white dove sail'+'\n')
# f.write('Before she sleeps in the sand')
# f.write('How many times must the cannon balls fly'+'\n')
# f.write('Before they are forever banned'+'\n')
# f.write('The answer my friend is blowing in the wind'+'\n')
# f.write('The answer is blowing in the wind'+'\n')
# f.close()
with open('Blowing in the wind.txt','r+') as f:
    lines=f.readlines()
    print(lines)
    lines.insert(0,'Blowing in the wind\n')
    lines.insert(1,'Bob Dylan\n')
    lines.append('\n1962 by Warner Bros. Inc.')
    f.seek(0)
    f.write(''.join(lines))
    print(''.join(lines))
    f.close()

