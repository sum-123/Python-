#   设计一个留言本的表（ID，留言内容，留言人，留言时间，是否删除）（表名，和字段名自己设计成英文：注意，不要用中文，用中文的直接0分）；
#   使用SQLAlchemy驱动模块，实现对这个表的增加，删除，修改，查询；数据库操作需要加入异常处理逻辑；

from sqlalchemy import Column, String, create_engine, Integer
from sqlalchemy.orm import choosemaker
from sqlalchemy.ext.declarative import declarative_base
import datetime

Base = declarative_base()

class Message(Base):
    # 表的名字
    __tablename__ = 'messageboard'

    # 表的结构
    ID = Column(Integer, primary_key = True)
    COMMENT = Column(String(50))
    USER_NAME = Column(String(20))
    DATE = Column(String(30))
    IS_DELETE = Column(Integer)


# 初始化数据库连接
engine = create_engine('mysql+mysqlconnector://root:qazwsx123@localhost:3306/test')

# 创建DBchoose类型
DBchoose = choosemaker(bind = engine)


def result(choice):
    if choice == 1:
        choose = DBchoose()
        id = int(input("请输入留言序号："))
        comment = input("请输入留言内容：")
        user_name = input("请输入您的姓名：")
        date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        is_delete = 0

        new_message = Message(ID = id, COMMENT = comment, USER_NAME = user_name, DATE = date, IS_DELETE = is_delete)
        choose.add(new_message)
        choose.commit()
        choose.close()
        print("留言已添加！")

    if choice == 2:
        choose = DBchoose()
        id_chosen = int(input("请输入要删除的留言序号："))
        message_delete = choose.query(Message).filter_by(ID = id_chosen).one()
        message_delete.IS_DELETE = 1
        choose.commit()
        choose.close()
        print("留言已删除！")

    if choice == 3:
        choose = DBchoose()
        id_chosen = int(input("请输入要修改的留言序号："))
        comment = input("请输入修改后的留言：")
        date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        message_revise = choose.query(Message).filter_by(ID = id_chosen).one()
        message_revise.COMMENT = comment
        message_revise.DATE = date
        choose.commit()
        choose.close()
        print("留言已修改！")

    if choice == 4:
        choose = DBchoose()
        message = choose.query(Message).filter().all()
        for i in message:
            print("ID:{0}, COMMENT:{1}, USER_NAME:{2}, DATE:{3}, IS_DELETE:{4}".format(i.ID, i.COMMENT, i.USER_NAME, i.DATE, i.IS_DELETE))
        choose.commit()
        choose.close()

if __name__ == '__main__':
    print("欢迎来到留言板！")
    while True:
        print("1. 添加留言")
        print("2. 删除留言")
        print("3. 修改留言")
        print("4. 查询留言")
        print("5. 退出留言板")
        choice = int(input("请输入要进行的操作："))
        if choice == 5:
            print("留言板已退出！")
            break
        else:
            result(choice)