from flask import Flask, render_template

# 实例化对象
from flask_script import Manager

app = Flask(__name__)

# 初始化配置
manager = Manager(app)



@app.route('/') # 路由
def hello_world():  # 视图函数
    return 'hello world'


@app.route('/home/')
def home():
    return '首页 | uu'

@app.route('/cart/')
def cart():
    return render_template('cart.html')


if __name__ == '__main__':
    manager.run()


# 需求: 能不能像Django启动项目
# 解决: 安装插件 flask-script
# 作用: 解析命令行参数(接受命令行参数)


## 插件一般集成流程
# 1、查看官方文档(如何使用)
# 2、安装
# 3、配置
# 4、使用


##
# 1、文档: https://flask-script.readthedocs.io/en/latest/
# 2、安装: pip install Flask-Script
# 3、配置: manager = Manager(app)  manager.run()
# 4、使用: python manage.py runserver
#  python manage.py runserver -r -d
#  python manage.py runserver -r -d -p 8000