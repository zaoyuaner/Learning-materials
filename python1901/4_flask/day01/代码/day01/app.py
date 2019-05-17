import datetime
import os
import sys
import uuid

from flask import Flask, request
from flask_script import Manager

# 获取flask对象，初始化基础的配置
app = Flask(__name__)

# 定义路由地址: ‘/’，和处理方法hello()
@app.route('/hello/')
def hello():
    return 'hello world'

# 访问路由地址为: /article/?pk=1
@app.route('/article/')
def article():
    pk = request.args['pk']
    print(request)
    return '文章详情'

# 路由匹配规则: <转换器:参数名>
# 转换器，int, string(默认的类型), float, uuid


# 访问路由地址为: /article/23/
@app.route('/article/<int:id>/')
def acticle_detail(id):
    # 通过id查询数据库中文章表的内容
    return '文章id为: %s' % id


@app.route('/article/<string:title>/')
def article_title(title):
    return '文章title为:%s' % title


@app.route('/art_title/<title>/')
def art_title(title):
    print(type(title))
    return '文章title为：%s' % title


@app.route('/art_float/<float:price>/')
def art_float(price):
    return '浮点数float为: %s' % price


@app.route('/get_uuid/')
def get_uuid():
    a = uuid.uuid4()
    return 'uuid: %s' % str(a)


@app.route('/art_uuid/<uuid:uid>/')
def art_uuid(uid):
    return 'uuid值为：%s' % uid






if __name__ == '__main__':
    # 启动flask程序
    # 1. flask自带启动方式
    # app.run(host='127.0.0.1', port=8000, debug=True)
    # 2. 优化启动命令，启动参数从命令中获取
    # print(sys.argv)
    # python app.py 127.0.0.1 8000
    # host = sys.argv[1]
    # port = sys.argv[2]
    # app.run(host=host, port=port, debug=True)
    # 3. 使用flask-script库
    manage = Manager(app)
    manage.run()


