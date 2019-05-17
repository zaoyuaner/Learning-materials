import time

from flask_restful import Resource, fields, marshal_with
from app.models import Goods


goods_fields = {
    'name': fields.String,
    'img': fields.String,
    'price':fields.Integer,
}

result_fields = {
    'msg': fields.String,
    'status': fields.Integer,
    'date': fields.String,
    'goods': fields.Nested(goods_fields),
}


class GoodsResource(Resource):
    @marshal_with(result_fields)
    def get(self):
        goods = Goods.query.all()
        response_data = {
            'msg': '获取商品数据成功',
            'status': 200,
            'date': str(time.time()),
            'goods': goods,

        }

        return response_data


