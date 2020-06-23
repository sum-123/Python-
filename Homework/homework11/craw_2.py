import threading
from queue import Queue
import requests
from lxml import etree
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from config import DB_URL
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine.base import Engine

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
        # max_overflow = 50,  # 超过连接池大小之后，允许最大扩展连接数；
        # pool_size = 50,  # 连接池的大小
        # pool_timeout = 600,  # 连接池如果没有连接了，最长的等待时间
        # pool_recycle = -1,  # 多
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
session = creat_session()

def orm_insert(positon, company,address,salary,date):
    obj = data_table(POSITION=positon, COMPANY=company,ADDRESS=address,SALARY=salary,DATE=date)  # 生成数据对象
    session.add(obj)  # 把要创建的数据对象添加到session里
    session.commit()  # 创建数据


HEADRES = {
    'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.6788.400 QQBrowser/10.3.2864.400',
}
COUNT = 0


class Producters(threading.Thread):
    def __init__(self, page_queue, content_queue, *args, **kwargs):
        super(Producters, self).__init__(*args, **kwargs)
        self.page_queue = page_queue
        self.content_queue = content_queue

    def run(self):
        while True:
            if self.page_queue.empty():
                break
            url = self.page_queue.get()
            self.parse_html(url)

    def getHtml(self, url):
        r = requests.get(url, headers=HEADRES,timeout=2)
        r.encoding = r.apparent_encoding
        return r.text

    def parse_html(self, url):
        text = self.getHtml(url)
        # print(text)
        html = etree.HTML(text)
        divs = html.xpath('//div[@class="el"]')
        for div in divs[4:]:
            spans = div.xpath('.//span')
            try:
                jobname = spans[0].xpath('./a/text()')[0]
                # print(spans[0].xpath('./a/text()')[0])
                companyname = spans[1].xpath('.//text()')[0]
                address = spans[2].xpath('.//text()')[0]
                salary = spans[3].xpath('.//text()')[0]
                time = spans[4].xpath('.//text()')[0]
                # print(jobname.strip(), companyname, address, salary, time+'\n')
                print('companyname' + companyname)
                self.content_queue.put(
                    [jobname.strip() + '$', companyname + '$', address + '$', salary + '$', time + '\n'])
            except:
                continue


class Customer(threading.Thread):
    def __init__(self, page_queue, content_queue, *args, **kwargs):
        super(Customer, self).__init__(*args, **kwargs)
        self.page_queue = page_queue
        self.content_queue = content_queue

    def run(self):
        global COUNT
        while True:
            if self.content_queue.empty() and self.page_queue.empty():
                break
            orm_insert(self.content_queue.get()[0],self.content_queue.get()[1], self.content_queue.get()[2],self.content_queue.get()[3],self.content_queue.get()[4])
            # with open('java1job.txt', 'a+', encoding='utf-8') as f:
            #     print(COUNT)
            #     COUNT += 1
            #     f.writelines(self.content_queue.get())


if __name__ == '__main__':
    page_queue = Queue(2000)
    content_queue = Queue(100000)
    for i in range(1, 1000):
        page_queue.put('https://search.51job.com/list/000000,000000,0000,00,9,99,python,2,' + str(
            i) + '.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare=')
    # for x in range(5):
    t = Producters(page_queue, content_queue)
    t.start()
    # for x in range(5):
    t = Customer(page_queue, content_queue)
    t.start()
