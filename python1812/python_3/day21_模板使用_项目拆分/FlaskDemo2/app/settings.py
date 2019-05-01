import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


class BaseConfig(object):
    SECRET_KEY = '$%^&*()123123retyuifghjkKL:"M<'
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopConfig(BaseConfig):
    DEBUG = True
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///develop.db'
    # SQLALCHEMY_DATABASE_URI = 'sqlite:////' + os.path.join(BASE_DIR, '../develop.db')
    SQLALCHEMY_DATABASE_URI = 'sqlite:////' + os.path.join(BASE_DIR, 'develop.db')


class TestingConfig(BaseConfig):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///testing.db'


class StagingConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///stating.db'


class ProductConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///product.db'


config = {
    'develop': DevelopConfig,   # 开发环境
    'testing': TestingConfig,   # 测试环境
    'staging': StagingConfig,   # 演示环境
    'product': ProductConfig,   # 生产环境
    'default': DevelopConfig,   # 默认
}

def init_app(app, env_name):
    app.config.from_object(config.get(env_name))


