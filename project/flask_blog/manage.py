import redis
from flask import Flask
from flask_script import Manager
from flask_session import Session

from back.models import db
from back.views import back_blue
from web.views import web_blue

app = Flask(__name__)
# 配置路由（前后台分开）
app.register_blueprint(blueprint=back_blue,url_prefix='/back')  # 注册蓝图，url_prefix指定路径前缀
app.register_blueprint(blueprint=web_blue,url_prefix='/web')

# 配置mysql数据库mysql+pymysql://root:=@127.0.0.1:3306/blog
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:=@127.0.0.1:3306/blog'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# 配置缓存
app.config['SESSION_TYPE'] = 'redis'
app.config['SESSION_REDIS'] = redis.Redis(host='127.0.0.1',port=6379)
# 配置秘钥种子
app.secret_key = 'sdf23#$2s#$fdgsd432dsf4$%&sd@G4'

# 初始化配置
Session(app)
db.init_app(app)
manager = Manager(app)


if __name__ == '__main__':

    manager.run()