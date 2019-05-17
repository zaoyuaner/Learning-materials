from flask import Blueprint

from app.ext import db
from app.models import User

blue = Blueprint('blue', __name__)

def init_view(app):
    app.register_blueprint(blueprint=blue)


@blue.route('/')
def index():
    return 'hello flask!'

@blue.route('/createall/')
def createall():

    db.create_all()

    return '创建成功'


