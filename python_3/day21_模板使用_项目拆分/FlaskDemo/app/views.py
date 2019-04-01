import random

from flask import Blueprint, request, render_template, session, redirect, url_for

from app import db
from app.models import User

blue = Blueprint('blue', __name__)


@blue.route('/')
def index():

    # 状态保持
    username = session.get('username')

    # names = ['张三', '李四', '王五']

    return render_template('index.html', username=username, tempstr='helloWord')


@blue.route('/login/', methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        username = request.form.get('username')

        # 去数据库检索

        # 状态保持
        session['username'] = username

        return redirect(url_for('blue.index'))


@blue.route('/register/', methods=['GET','POST'])
def register():
    pass

@blue.route('/logout/')
def logout():
    # 方式一: session依赖于cookie
    # response = redirect(url_for('blue.index'))
    # response.delete_cookie('session')

    # 方式二: session
    session.pop('username')

    return redirect(url_for('blue.index'))


@blue.route('/cart/')
def cart():

    name = 'uu'

    return render_template('cart.html', name=name)


@blue.route('/createall/')
def createall():

    db.create_all()

    return '创建成功'


@blue.route('/adduser/')
def adduser():
    user = User()
    user.name = str(random.randrange(10000)) + '-uu'
    user.password = str(random.randrange(100000,1000000))

    # 保存
    db.session.add(user)
    db.session.commit()

    return '添加用户成功'


@blue.route('/showuser/')
def showuser():
    users = User.query.all()

    return render_template('showuser.html', users=users)
