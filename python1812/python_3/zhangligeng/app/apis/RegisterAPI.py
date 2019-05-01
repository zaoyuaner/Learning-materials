import time
import uuid
from flask import render_template, url_for
from flask_mail import Message
from flask_restful import Resource, reqparse, fields, marshal_with
from werkzeug.security import generate_password_hash

from app.ext import db, cache
from app.models import User

# 请求格式定制
parser = reqparse.RequestParser()
parser.add_argument('username', type=str, required=True, help='请提供用户名')
parser.add_argument('password', type=str, required=True, help='请提供密码')
parser.add_argument('email', type=str, required=True, help='请提供邮箱')

# 响应格式定制
"""
{
    'msg':'登录成功',
    'status':200,
    'date':'5454545',
    'user':{
        'username':'1asdf',
        'icon':'/static/img/a.png'
        'permissions':1,        
        }
    'token':'121654',

}

"""


class IconFomat(fields.Raw):
    def format(self, value):
        return '/static/img/' + value


user_fields = {
    'username': fields.String,
    'icon': IconFomat(attribute='icon'),
    'permissions': fields.Integer
}

result_fields = {
    'msg': fields.String,
    'status': fields.Integer,
    'date': fields.String,
    'user': fields.Nested(user_fields),
    'token': fields.String
}


class RegisterResource(Resource):
    @marshal_with(result_fields)
    def post(self):
        parse = parser.parse_args()
        user = User()
        user.username = parse.get('username')
        user.password = generate_password_hash(parse.get('password'))
        user.email = parse.get('email')

        response_data = {
            'date': str(time.time()),
            'status': 404,
            'user': '',
            'token': '',
        }

        users = User.query.filter(User.username == user.username)
        if users.count():
            response_data['msg'] = '注册失败，用户名已存在，请重新注册！'
            return response_data

        users = User.query.filter(User.email == user.email)
        if users.count():
            response_data['msg'] = '注册失败，邮箱已存在，请重新注册！'
            return response_data

        db.session.add(user)
        db.session.commit()

        # 状态保持
        token = uuid.uuid5(uuid.uuid4(), 'register').hex
        cache.set(token, user.id, timeout=60 * 5)


        response_data['status'] = 200
        response_data['user'] = user
        response_data['msg'] = '注册成功!!!'
        response_data['token'] = token

        return render_template(url_for('blue.index'))