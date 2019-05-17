import os

from flask_bootstrap import Bootstrap
from flask_caching import Cache
from flask_debugtoolbar import DebugToolbarExtension
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from app.settings import BASE_DIR

db = SQLAlchemy()
migrate = Migrate()
cache = Cache(config={
    # filesystem
    # 'CACHE_TYPE': 'filesystem',
    # 'CACHE_DIR': os.path.join(BASE_DIR, 'cachedir')

    # redis
    'CACHE_TYPE': 'redis',
    'CACHE_KEY_PREFIX': 'flask(cache)'
})

def init_ext(app):
    db.init_app(app)
    migrate.init_app(app=app, db=db)
    Bootstrap(app)
    # toolbar = DebugToolbarExtension(app)
    cache.init_app(app)
