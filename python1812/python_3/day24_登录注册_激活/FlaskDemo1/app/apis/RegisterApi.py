import time
import uuid
from flask import render_template
from flask_mail import Message
from flask_restful import Resource,reqparse, fields, marshal_with

# 请求格式定制
from werkzeug.security import generate_password_hash

from app.ext import db, cache, mail
from app.models import User

parser = reqparse.RequestParser()
parser.add_argument('username', type=str, required=True, help='请提供用户名')
parser.add_argument('password', type=str, required=True, help='请提供密码')
parser.add_argument('email', type=str, required=True, help='请提供邮箱')

# 响应格式定制
"""
{
    'msg': '注册成功',
    'status': 200,
    'date': 'xxxxxxxx',
    'user': {
        'username': 'uu',
        'icon': '/static/img/atom.png/',
        'permissions': 1,
    },
    'token': 'xxxxxxxx',
}
"""

class IconFormat(fields.Raw):
    def format(self, value):
        return '/static/img/' +value


user_fields = {
    'username': fields.String,
    'icon': IconFormat(attribute='icon'),
    'permissions': fields.Integer,
}

result_fields = {
    'msg': fields.String,
    'status': fields.Integer,
    'date': fields.String,
    'user': fields.Nested(user_fields, default={}),
    'token': fields.String
}


class Register(Resource):
    @marshal_with(result_fields)
    def post(self):
        parse = parser.parse_args()
        user = User()
        user.username = parse.get('username')
        user.password = generate_password_hash(parse.get('password'))
        user.email = parse.get('email')

        response_data = {
            'date': str(time.time()),

        }

        # 数据处理
        response_data['status'] = 406
        response_data['user'] = ''
        users = User.query.filter(User.username == user.username)
        if users.count():  # 存在
            response_data['msg'] = '用户名已存在，注册失败!'
            return response_data

        users = User.query.filter(User.email == user.email)
        if users.count():
            response_data['msg'] = '邮箱已存在，注册失败!'
            return response_data


        # 存入数据库
        db.session.add(user)
        db.session.commit()


        # 状态保持
        token = uuid.uuid5(uuid.uuid4(), 'regisger').hex
        cache.set(token, user.id, timeout=60*10)

        # 发送邮件
        active_url = 'http://127.0.0.1:5000/api/v1/active/?token=' + token
        tempplate_str = render_template('mail_active.html',active_url=active_url, username=user.username)
        msg = Message(
            subject='AXF激活邮件',  # 主题
            sender='18924235915@163.com',   # 发件人
            recipients=[user.email],    # 收件人
            html=tempplate_str   # 正文
        )
        mail.send(msg)

        # 返回数据
        response_data['msg'] = '注册成功'
        response_data['status'] = 200
        response_data['user'] = user
        response_data['token'] = token

        return response_data







