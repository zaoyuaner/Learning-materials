
class BaseConfig(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@127.0.0.1:3306/python18120327'


config = {
    'develop': DevelopConfig,
    'default': DevelopConfig
}

def init_settings(app, env_name):
    app.config.from_object(config.get(env_name))