from flask import Blueprint, jsonify, request
from flask_restful import Resource

blue = Blueprint('blue', __name__)

def init_views(app):
    app.register_blueprint(blueprint=blue)


@blue.route('/')
def index():
    return 'hello flask!'


@blue.route('/jsontest/')
def jsontest():

    dir = {
        'msg': '获取数据成功',
        'status': 200,
        'data': '哈哈'
    }

    return jsonify(dir)


## https://www.douban.com/
## http://api.douban.com/v2/movie/top250


## www.baidu.com
## www.baidu.com/api/


@blue.route('/api/v1/student/', methods=['GET', 'POST', 'DELETE', 'PUT'])
def student():
    if request.method == 'GET': # 获取学生列表
        pass
    elif request.method == 'POST':  # 添加学生
        pass
    elif request.method == 'PUT':   # 更新学生
        pass
    elif request.method == 'DELETE':    # 删除学生
        pass



##################### RESTful #####################
# # 定义资源
# class HelloWord(Resource):
#     def get(self):
#         return {'msg':'[get]hello'}
#
#     def post(self):
#         return {'msg':'[post]hello'}
#
# # 添加资源
# api.add_resource(HelloWord, '/api/v1/hello/')