import redis
from flask import Flask, request, make_response, \
    render_template, session, redirect
from flask_script import Manager
from flask_session import Session

from utils.functions import login_required

app = Flask(__name__)
# 加密方式
app.secret_key = 'aoshdoahfjrht0eiarh93q7493'
# 配置session数据库信息
app.config['SESSION_TYPE'] = 'redis'
app.config['SESSION_REDIS'] = redis.Redis(host='127.0.0.1', port=6379)
# 配置方法: 第一种
Session(app)
# 配置方法: 第二种
# sess = Session()
# sess.init_app(app)

# /article/?pk=2  GET
# /article/2/  POST


@app.route('/')
def hello():
    return 'hello world'


@app.route('/article/<int:id>/', methods=['GET', 'POST'])
@login_required
def update_article(id):
    # 请求 request
    if request.method == 'GET':
        # 模拟查询数据库中的文章表
        return '获取文章成功'
    if request.method == 'POST':
        return '修改文章成功'


@app.route('/login/', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        # 取post请求传递的数据
        # request.form 获取值
        # getlist(key) ===>  [key对应的value值组装的列表]
        pass
    if request.method == 'GET':
        # request.args 获取值
        # getlist(key) ===>  [key对应的value值组装的列表]
        pass

# 响应
@app.route('/response/', methods=['GET'])
def get_response():
    # 响应为服务器发送给浏览器
    # 创建响应对象
    # res = make_response('hello', 404)
    # res = make_response('<h2>hello</h2>', 200)
    # html = render_template('index.html')
    # res = make_response(html)
    # return res

    # make_response 有用的情况
    # 使用cookie的情况
    res = make_response('给你一把钥匙')
    # 存入前女友家的钥匙
    # res.set_cookie('token', '1234567890', max_age=300)
    # 前女友收回钥匙
    res.delete_cookie('token')
    return res


@app.route('/home/')
def home():
    # 校验访问该方法时，校验码token是否正确
    # 如果正确则返回响应页面index.html，否则返回’你没有权限进入我的门‘
    token = request.cookies.get('token')
    if not token:
        return '你没有权限进入我的门'
    if token != '1234567890':
        return '校验token失败，还是没权限进入'
    return render_template('index.html')


@app.route('/my_login/', methods=['GET', 'POST'])
def my_login():
    if request.method == 'GET':
        return render_template('login.html')

    if request.method == 'POST':
        # 登录的校验
        username = request.form.get('username')
        password = request.form.get('password')
        # 模拟登陆
        if username == 'coco' and password == '123456':
            # 登录成功，给与标识符（钥匙）
            res = make_response(render_template('index.html'))
            res.set_cookie('token', '1234567890', max_age=300)
            return res
        return render_template('login.html')


@app.route('/session_login/', methods=['GET', 'POST'])
def session_login():
    if request.method == 'GET':
        return render_template('login.html')

    if request.method == 'POST':
        # 模拟登陆
        username = request.form.get('username')
        password = request.form.get('password')
        if username == 'coco' and password == '123456':
            # 模拟登陆成功，给前端一个标识符(sessionid)，后端校验该标识符
            session['username'] = 'coco'
            session['age'] = 18
            # return render_template('index.html')
            return redirect('/home/')
        return render_template('login.html')


@app.route('/session_home/', methods=['GET'])
def session_home():
    # 校验登录状态
    username = session.get('username')
    if not username:
        return render_template('login.html')
    return render_template('index.html')

# 使用装饰器去实现登录校验的功能
# @login_required
# 外层函数嵌套内层函数
# 外层函数返回内层函数
# 内层函数调用外层函数的参数


@app.route('/session_index/', methods=['GET'])
@login_required
def session_index():

    return render_template('index.html')


if __name__ == '__main__':
    manage = Manager(app)
    manage.run()


