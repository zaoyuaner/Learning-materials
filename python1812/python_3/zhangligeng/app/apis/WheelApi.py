import time

from flask_restful import Resource, fields, marshal_with
from app.models import Wheel


wheel_fields = {
    'name': fields.String,
    'img': fields.String,
}

result_fields = {
    'msg': fields.String,
    'status': fields.Integer,
    'date': fields.String,
    'wheels': fields.Nested(wheel_fields),
}


class WheelResource(Resource):
    @marshal_with(result_fields)
    def get(self):
        wheels = Wheel.query.all()
        response_data = {
            'msg': '获取轮播图数据成功',
            'status': 200,
            'date': str(time.time()),
            'wheels': wheels,

        }

        return response_data


