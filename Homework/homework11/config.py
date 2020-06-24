# SQLAlchemy连接数据库的配置信息

HOST_NAME = 'localhost'
PORT = '3306'
DATABASE = 'test'
USER_NAME = 'root'
PASSWORD = 'qazwsx123'

DB_URL = f'mysql+pymysql://{USER_NAME}:{PASSWORD}@{HOST_NAME}:{PORT}/{DATABASE}?charset=utf8'

