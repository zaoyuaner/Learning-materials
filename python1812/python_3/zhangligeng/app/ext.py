from flask_caching import Cache
from flask_mail import Mail
from flask_migrate import Migrate
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
migrate = Migrate()
cache = Cache(config={'CACHE_TYPE':'redis'})


def init_ext(app):
    db.init_app(app)
    migrate.init_app(app=app,db=db)
    cache.init_app(app)