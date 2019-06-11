# encoding :utf-8
from flask_script import Manager

#这里不是主程序了，用再传app
DBmanager = Manager()

@DBmanager.command
def init():
    print('数据库初始化')

@DBmanager.command
def migrate():
    print('数据库迁移成功')


