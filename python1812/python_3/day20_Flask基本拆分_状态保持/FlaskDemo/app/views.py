import uuid

from flask import Blueprint, request, render_template, make_response, Response, redirect, url_for, abort

blue = Blueprint('simple_page', __name__)

# app是Flask实例
# @blue.route('/')
# @blue.route('/home/')
# @blue.route('/haha/')
# def hello_world():
#     return 'Hello sWorld!'


#### 路径参数
# 默认的类型是string
# 一一对应
@blue.route('/setname/<name>/')
def setname(name):
    return '名字:' + name

@blue.route('/setage/<int:age>/')
def setage(age):
    return '年龄:' + str(age)

@blue.route('/setscore/<float:score>/')
def setscore(score):
    return '成绩:' + str(score)

@blue.route('/sum/<int:a>/<int:b>/<int:c>/')
def sum(a,b,c):
    return '{} + {} + {} = {}'.format(a,b,c, (a+b+c))

@blue.route('/setuuid/<uuid:uu>/')
def setuuid(uu):
    return '已经登录'

@blue.route('/getuuid/')
def getuuid():
    return str(uuid.uuid4())

@blue.route('/getop/<any(A,B,C):op>/')
def getop(op):
    return '套餐类型:' + op

@blue.route('/getpath/<path:where>/')
def getpath(where):
    return '我的位置:' + where


#### 请求类型
@blue.route('/methodstest/', methods=['GET','POST','PUT', 'DELETE'])
def methodstest():
    return '请求方法测试'


#### Request请求对象
@blue.route('/requesttest/', methods=['POST','GET'])
def requesttest():
    data = {
        '请求方式': request.method,
        '请求路径': request.path,
        '请求URL': request.url,
        'GET请求参数': request.args,
        'POST请求参数': request.form,
        '文件参数': request.files,
        'cookie': request.cookies
    }

    return str(data)


#### Response响应
@blue.route('/responsetest/')
def responsetest():
    # return 'hello'
    # return 'hello',300

    # template = render_template('responsetest.html')
    # print(type(template))
    # return template,300

    # response = make_response('hello')

    # template = render_template('responsetest.html')
    # response = make_response(template)


    # response = Response('hello')
    # response = Response('hello', 404)

    # response = redirect('/requesttest/')

    # 反向解析
    # url_for('蓝图名.视图名')
    url_path = url_for('simple_page.requesttest')
    response = redirect(url_path)

    return response


#### 抛出异常
@blue.route('/errtest/')
def errtest():
    # abort(403)
    abort(500)

# 异常捕获
@blue.errorhandler(403)
def err403(err):
    return '<h1>我不是403!</h1>'


@blue.errorhandler(500)
def err500(err):
    return '<h1>试试看---500</h1>'




#### 状态保持 cookie
@blue.route('/')
def index():
    # 状态保持
    name = request.cookies.get('username', '未登录')
    age = 30

    return render_template('index.html', uesrname=name, age=age)

@blue.route('/login/', methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        name = request.form.get('username')
        response = redirect(url_for('simple_page.index'))
        response.set_cookie('username', name, max_age=60)
        return response


@blue.route('/register/', methods=['GET','POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    elif request.method == 'POST':
        name = request.form.get('username')

        # 状态保持
        response = redirect(url_for('simple_page.index'))
        response.set_cookie('username', name, max_age=60*60)

        # 返回首页
        return response

@blue.route('/logout/')
def logout():
    response = redirect(url_for('simple_page.index'))
    response.delete_cookie('username')

    return response

