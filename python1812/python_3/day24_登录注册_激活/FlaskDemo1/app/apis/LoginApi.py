import time
import uuid

from flask import render_template
from flask_mail import Message
from flask_restful import Resource, reqparse, fields, marshal_with
from werkzeug.security import check_password_hash

from app.ext import cache, mail
from app.models import User

parser = reqparse.RequestParser()
parser.add_argument('username', type=str, required=True, help='请提供用户名')
parser.add_argument('password', type=str, required=True, help='请提供密码')

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



class Login(Resource):
    @marshal_with(result_fields)
    def post(self):
        parse = parser.parse_args()
        username = parse.get('username')
        password = parse.get('password')

        response_data = {
            'date': str(time.time()),
            'status': 406
        }

        users = User.query.filter(User.username == username)
        if users.count():   # 存在
            user = users.first()
            if check_password_hash(user.password, password):  # 验证通过
                # 删除
                if user.isdelte:
                    response_data['msg'] = '登录失败，用户不存在'
                    return response_data

                # 状态保持
                token = uuid.uuid5(uuid.uuid4(), 'regisger').hex
                cache.set(token, user.id, timeout=60 * 10)

                # 激活
                if user.isactive:
                    response_data['msg'] = '登录成功'
                    response_data['status'] = 200
                    response_data['user'] = user
                    response_data['token'] = token
                    return response_data
                else:
                    # 发送邮件
                    active_url = 'http://127.0.0.1:5000/api/v1/active/?token=' + token
                    tempplate_str = render_template('mail_active.html', active_url=active_url, username=user.username)
                    msg = Message(
                        subject='AXF激活邮件',  # 主题
                        sender='18924235915@163.com',  # 发件人
                        recipients=[user.email],  # 收件人
                        html=tempplate_str  # 正文
                    )
                    mail.send(msg)

                    response_data['msg'] = '登录失败，用户未激活。激活邮件已经重新发送，请注意查看邮箱!'
                    return response_data
            else:
                response_data['msg'] = '登录失败，密码错误'
                return response_data
        else:   # 不存在
            response_data['msg'] = '登录失败，用户名不存在'
            return response_data
