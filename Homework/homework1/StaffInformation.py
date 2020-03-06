# -*- encoding: utf-8 -*-
'''
@File : StaffInformation.py
@Time : 2020/03/06 13:49:38
@Author : zjm 
@Version : 1.0
@Contact : 1005564803@qq.com
@WebSite : https://github.com/sum-123/Python-.git
'''

# here put the import lib
list=[('10001','张三',5,3600),('10002','李四',5,3400),('10003','王武',6,3800),('10004','李林',5,4300),('10005','李华',7,8900),
('10006','赵龙',2,6600),('10007','刘虎',3,3300),('10008','刘强',5,9500),('10009','张名',5,3400),('10010','柳青',8,3400)]
for a,b,c,d in list:
    print('工号: ',a,'姓名: ',b,'工龄:',c,'工资:',d)
