# -*- encoding: utf-8 -*-
'''
@File : dictclass.py
@Time : 2020/04/17 11:16:25
@Author : zjm 
@Version : 3.7.6
@Contact : 1005564803@qq.com
@WebSite : https://github.com/sum-123/Python-.git
'''

# here put the import lib
class dictclass():
    def __init__(self,dict):
         self.dict=dict
    def del_dict(self,key):
        if key in self.dict.keys():
            del self.dict[key]
            return self.dict
        else:
            return 'not exist'
    def get_dict(self,key):
        if key in self.dict.keys():
            return self.dict[key]
        else:
            return 'not found'
    def get_key(self):
        return list(self.dict.keys())
    def update_dict(self,dict1):
        self.dict.update(dict1)
        return self.dict
dic = dictclass({"姓名": "Jack", "年龄": "17", "性别": "女"})
print(dic.del_dict("年龄"))
print(dic.get_dict("姓名"))
print(dic.get_key())
print(dic.update_dict({'学号':123}))




     
          
