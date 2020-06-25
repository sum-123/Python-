from bs4 import BeautifulSoup
from urllib.request import urlopen
import threading
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from config import DB_URL
from sqlalchemy.orm import sessionmaker
import sys, time
from data_clean import data_clean
from calculate import calculate_salary

Base = declarative_base()


class data_table(Base):
    __tablename__ = 'Jobs'
    id = Column(Integer, primary_key=True)
    POSITION = Column(String(100))
    COMPANY = Column(String(100))
    ADDRESS = Column(String(100))
    SALARY = Column(String(100))
    DATE = Column(String(100))


def init_db():
    engine = create_engine(
        DB_URL,
        encoding="utf-8",
        echo=True
    )
    Base.metadata.create_all(engine)
    print('Create table successfully!')


init_db()

connect = create_engine(DB_URL)


def creat_session():
    # 创建与数据库的会话session class ,这里返回给session的是class
    session_class = sessionmaker(bind=connect)
    # 生成session实例
    return session_class()


header = {
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36",
    "Accept": " text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Encoding": "gzip,deflate",
    "Accept-Language": "zh-CN,zh;q=0.8"
};

avg_salary = 0


def get_info(url):
    global avg_salary

    html = urlopen(url).read().decode('GBK')

    soup = BeautifulSoup(html, "html.parser")
    # 获取职位信息
    titles = soup.select("p[class='t1'] a")
    # 获取工作地点
    di = soup.select("span[class='t3']")
    # 获取公司
    company = soup.select("span[class='t2']")
    # 获取薪水信息
    salaries = soup.select("span[class='t4']")  # CSS 选择器
    # 获取发布时间
    time = soup.select("span[class='t5']")

    for i in range(len(titles)):
        # with open("1.txt","a") as f:

        #     f.write(titles[i].get('title'))
        #     f.write(salaries[i+1].get_text())
        #     f.write("\n")
        # print("{:30}{}{}".format(titles[i].get('title'),salaries[i+1].get_text(),di[i+1].get_text()),company[i+1].get_text())
        if ("Python" or "python") in titles[i].get('title') and "开发工程师" in titles[i].get('title'):
            # 数据清洗完成单位转换

            m = data_clean(salaries[i + 1].get_text())
            # 筛选北京地区Python开发工程师
            if "北京" in di[i + 1].get_text():
                avg_salary = calculate_salary(m)

            session = creat_session()
            try:

                obj = data_table(POSITION=titles[i].get('title'), COMPANY=company[i + 1].get_text(),
                                 ADDRESS=di[i + 1].get_text(), SALARY=m, DATE=time[i + 1].get_text())  # 生成数据对象
                session.add(obj)  # 把要创建的数据对象添加到session里
                session.commit()
            except:
                continue
            # orm_insert(titles[i].get('title'),company[i+1].get_text(),di[i+1].get_text(),salaries[i+1].get_text(),time[i+1].get_text())


Count = 0


def option1():
    global Count
    for i in range(1, 200):
        url = url_ + str(i) + ".html"
        get_info(url)
        Count = Count + 1


def option2():
    global Count
    for i in range(201, 400):
        url = url_ + str(i) + ".html"
        get_info(url)
        # 实现爬取进度显示
        Count = Count + 1
        str1 = '>' * ((Count // 4) // 2) + ' ' * ((100 - (Count // 4)) // 2)
        sys.stdout.write('\r' + str1 + '[%s%%]' % ((Count / 4) + 1))
        sys.stdout.flush()
        time.sleep(0.1)


url_ = "https://search.51job.com/list/000000,000000,0000,00,9,99,Python,2,"


def multi_thread():
    t1 = threading.Thread(target=option1)
    t2 = threading.Thread(target=option2)
    t1.start()
    t2.start()
    print("正在爬取......")
    while True:

        if Count == 398:
            print('')
            print("爬取完成......")
            print('')
            print("*" * 50)
            print('')
            print("   北京Python开发工程师的平均薪资为%.2f万/月" % avg_salary)
            print('')
            print("*" * 50)
            break


multi_thread()
