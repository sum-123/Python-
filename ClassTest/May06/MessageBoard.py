# -*- encoding: utf-8 -*-
'''
@File : test5.py
@Time : 2020/05/06 20:08:14
@Author : zjm 
@Version : 3.7.6
@Contact : 1005564803@qq.com
@WebSite : https://github.com/sum-123/Python-.git
'''
#    创建一个留言板的表（ID，留言主题，留言人，留言时间）4个字段，注意，字段请用英文；
#    完成对这个表记录的增，删，改，查询；
#    用PyMySQL驱动方式

# here put the import lib
import pymysql
db = pymysql.connect("localhost","root","qazwsx123","test" )
 
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()
cursor.execute("DROP TABLE IF EXISTS MESSAGEBOARD")
# **********创建表**********
create = """CREATE TABLE MESSAGEBOARD (
         ID  CHAR(20) NOT NULL,
         THEME CHAR(20),
         NAME  CHAR(20),
         MESSAGE_TIME DATE 
          )"""
 
cursor.execute(create)
# **********增加数据*********
insert="""INSERT INTO MESSAGEBOARD(ID,
         THEME, NAME, MESSAGE_TIME)
         VALUES ('1201810801', 'Python','Jack', '2020-05-06')"""
try:
    cursor.execute(insert)
    db.commit()
except:
    db.rollback()
#***********查询记录*********
search="SELECT * FROM MESSAGEBOARD"
try:
   # 执行SQL语句
   cursor.execute(search)
   # 获取所有记录列表
   results = cursor.fetchall()
   for row in results:
      id = row[0]
      theme = row[1]
      name = row[2]
      time = row[3]
       # 打印结果
      print ("id = %s,theme = %s,name = %s,time = %s" % \
             (id, theme, name, time))
except:
   print ("Error: unable to fetch data")
#***********更新记录***********
upgrade="UPDATE MESSAGEBOARD SET THEME ='pyhon123' "
try:
   # 执行SQL语句
   cursor.execute(upgrade)
   # 提交到数据库执行
   db.commit()
except:
   # 发生错误时回滚
   db.rollback()
# *********删除记录************
delete = "DELETE FROM MESSAGEBOARD WHERE THEME > %s" % ('python123')
try:
   # 执行SQL语句
   cursor.execute(delete)
   # 提交修改
   db.commit()
except:
   # 发生错误时回滚
   db.rollback()

# 关闭数据库连接
db.close()
