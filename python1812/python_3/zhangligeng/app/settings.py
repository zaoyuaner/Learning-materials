import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

class BaseConfig(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = '!@#$%^&*()456789321ghosdajfoaijd<>'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = \
        'mysql+pymysql://root:335600@127.0.0.1:3306/python18120329'



config = {
    'develop': DevelopConfig,
    'default': DevelopConfig,
}

def init_app(app, env_name):
    app.config.from_object(config.get(env_name))