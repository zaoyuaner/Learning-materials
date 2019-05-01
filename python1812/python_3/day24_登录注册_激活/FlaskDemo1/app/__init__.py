from app.apis import init_apis
from app.ext import init_ext
from app.settings import init_settings
from app.views import init_views


def create_app(env_name='default'):
    from flask import Flask

    app = Flask(__name__)

    init_settings(app, env_name)

    init_ext(app)

    init_views(app)

    # 思路和蓝图一样
    init_apis(app)

    return app
