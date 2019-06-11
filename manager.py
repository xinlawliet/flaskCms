# encoding :utf-8
from flask_script import Manager
from app import app
from db_command import DBmanager


manager = Manager(app)

@manager.command
def runserver():
    print('服务器过一会就开，请稍等')

#将另外一个文件的命令添加到主命令文件中，'db'是子命令的开头（可随意更改），后导入dbmanager对象
manager.add_command('db',DBmanager)

# if __name__ == '__main__':
#     manager.run()
