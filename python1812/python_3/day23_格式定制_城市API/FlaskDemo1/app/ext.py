from flask_migrate import Migrate
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
migrate = Migrate()

def init_ext(app):
    db.init_app(app)
    migrate.init_app(app, db)
