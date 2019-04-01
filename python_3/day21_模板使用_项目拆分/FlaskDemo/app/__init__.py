from flask_session import Session
from flask_sqlalchemy import SQLAlchemy

from app.models import db
from app.views import blue


def create_app():
    from flask import Flask

    app = Flask(__name__)
    app.register_blueprint(blueprint=blue)

    # session 默认是没有持久化存储
    # 使用session，需要做配置
    app.config['SECRET_KEY'] = '@#$%^&*()dfghjuiko@#$%^&*()fghj123123123134gagu'


    ## flask-session
    # 配置方式一
    # SESSION_TYPE = 'redis'
    # app.config.from_object(__name__)
    # 配置方式二
    app.config['SESSION_TYPE'] = 'redis'


    # 初始化，方式一
    # Session(app)

    # 初始化，方式二
    sess = Session()
    sess.init_app(app)


    ## ORM
    # /// 相对路径
    # //// 绝对路径
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)


    return app