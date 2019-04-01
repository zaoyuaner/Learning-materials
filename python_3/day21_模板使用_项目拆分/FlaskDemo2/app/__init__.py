from app.ext import init_ext
from app.settings import init_app
from app.views import init_view


def create_app(env_name='default'):
    from flask import Flask

    app = Flask(__name__)

    # 配置
    init_app(app, env_name)

    # 扩展(插件)
    init_ext(app)

    # 视图
    init_view(app)

    return app