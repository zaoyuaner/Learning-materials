import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

class BaseConfig(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = '!@#$%^&*()456789321ghosdajfoaijd<>'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopConfig(BaseConfig):
    DEBUG = True

    # create_all: 没问题
    # migrate: 有问题
    # test.db 相对路径， 执行migrate命令是在manage.py文件，相对于manage.py
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'

    # python18120326
    # 使用的数据库+驱动://用户名:密码@主机:端口/数据库名称
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@127.0.0.1:3306/python18120326'


config = {
    'develop': DevelopConfig,
    'default': DevelopConfig,
}

def init_app(app, env_name):
    app.config.from_object(config.get(env_name))