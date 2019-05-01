import uuid

from flask import Blueprint, jsonify, request, render_template, \
    redirect, url_for, session, g
from flask_restful import Resource
from app.ext import cache, db
from app.models import User

blue = Blueprint('blue',__name__)

def init_views(app):
    app.register_blueprint(blueprint=blue)


@blue.before_request
def beforeview():
    token = session.get('token')
    if token:
        userid = cache.get(token)
        users = User.query.filter(User.id == userid)
        if users.count():
            g.user = users.first()
        else:
            g.user = None
    else:
        g.user = None


@blue.route('/')
def index():
    return render_template('index.html', user=g.user)


@blue.route('/register/', methods=['POST','GET'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    elif request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        email = request.form.get('email')

        users = User.query.filter(User.username == username)
        if users.count():
            return '用户已存在,请重新选择'
        users = User.query.filter(User.email == email)
        if users.count():
            return '邮箱已存在,请重新选择'


        user = User()
        user.username = username
        user.password = password
        user.email = email

        db.session.add(user)
        db.session.commit()
        token = uuid.uuid5(uuid.uuid4(), 'aa').hex

        cache.set(token, user.id, timeout=60 * 3)
        session['token'] = token

        return redirect(url_for('blue.index'))


@blue.route('/login/', methods=['POST','GET'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        users = User.query.filter(User.username == username).filter(
            User.password == password)

        if users.count():
            user = users.first()
            token = uuid.uuid5(uuid.uuid4(), 'aa').hex
            cache.set(token, user.id, timeout=60 * 3)
            session['token'] = token
            return redirect(url_for('blue.index'))

        else:
            return '登录失败,输入信息有误'


@blue.route('/logout/')
def logout():
    # session.pop('token')
    session.clear()
    return redirect(url_for('blue.index'))


