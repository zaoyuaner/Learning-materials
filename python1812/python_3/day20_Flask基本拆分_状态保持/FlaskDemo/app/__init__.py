from flask import Flask
from app.views import blue


def create_app():
    # app是Flask实例
    app = Flask(__name__)

    app.register_blueprint(blueprint=blue)

    return app



# 需求: 项目拆分(MTV)
# 问题: 关系混乱问题
# 解决: 插件flask-blueprint