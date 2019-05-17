from app.ext import init_ext
from app.settings import init_app
from app.views import init_view


def create_app(env_name='default'):
    from flask import Flask
    app = Flask(__name__)

    init_app(app, env_name)

    init_ext(app)

    init_view(app)

    return app