# https://blog.csdn.net/guofei_fly/article/details/85485173

import pymysql
import configparser
config=configparser.ConfigParser()
cfg_file=r"C:\Users\Administrator\Desktop\conf.ini"
config.read(cfg_file)
data=config.sections()
host=config.get('mysql','host')
port=config.get('mysql','port')
user=config.get('mysql','user')
passwd=config.get('mysql','passwd')
db=config.get('mysql','db')

# self.charset=config.get('mysql','charset')
conn=pymysql.connect(
host=host,
port=port,
user=user,
passwd=passwd,
db=db
    )
cursor=conn.cursor()
conn.close()
cursor.close()