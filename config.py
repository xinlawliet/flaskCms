# encoding:utf-8
# Enable debug mode
DEVELOPMENT = True

#dialect+driver://username:password@host:port/database
DIALECT='mysql'
DRIVER='pymysql'
USERNAME='root'
PASSWORD='123456'
HOST='127.0.0.1'
PORT='3306'
DATABASE='db_demo1'

SQLALCHEMY_DATABASE_URI="{}+{}://{}:{}@{}:{}/{}?charset=utf8".format(DIALECT,DRIVER,USERNAME,PASSWORD,HOST,PORT,DATABASE)

SQLALCHEMY_TRACK_MODIFICATIONS = False
