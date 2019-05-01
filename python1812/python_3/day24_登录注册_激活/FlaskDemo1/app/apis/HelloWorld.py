from flask_restful import Resource


# 定义资源
class HelloResource(Resource):
    def get(self):
        return {'msg': 'hello'}