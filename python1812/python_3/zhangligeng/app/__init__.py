from flask import Flask
from app.apis import init_api
from app.ext import init_ext
from app.settings import init_app
from app.views import init_views


def create_app(env_name = 'default'):

    app = Flask(__name__)

    init_app(app,env_name)

    init_views(app)

    init_ext(app)

    init_api(app)

    return app