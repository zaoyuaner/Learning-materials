import time

from flask_restful import Resource, fields, marshal_with, reqparse, marshal

from app.models import Letter

""" 响应数据示例
{
    'msg': '获取城市信息成功',
    'status': 200,
    'date': '567890',
    'data': {
        'A': [
            {   # 具体城市信息
                "id":170,
                "parentId":0,
                "regionName":"马鞍山",
                "cityCode":340500,
                "pinYin":"MAANSHAN"
            },
            ...
        ],
        'B': []
    }
}
"""
city_fields = {   # 具体城市信息
    "id": fields.Integer,
    "parentId": fields.Integer,
    "regionName": fields.String,
    "cityCode": fields.Integer,
    "pinYin": fields.String
}

letter_fields = {
    'A': fields.List(fields.Nested(city_fields)),
    'B': fields.List(fields.Nested(city_fields)),
}

result_fields = {
    'msg': fields.String,
    'status': fields.Integer,
    'date': fields.String,
    'data': fields.Nested(letter_fields)
}

class CityResource(Resource):
    # @marshal_with(result_fields)
    def get(self):


        """
        {
            'A': [],
            'B': [],
            'C': []
        }
        """
        data = {}   # 需要格式化的数据
        letter_fields_dynamic = {}  # 数据的格式定制

        letters = Letter.query.all()
        # 遍历
        for letter in letters:
            data[letter.name] = letter.citys
            # 动态生成 letter_fields
            # '*': fields.List(fields.Nested(city_fields)),
            letter_fields_dynamic[letter.name] = fields.List(fields.Nested(city_fields))


        response_data = {   # 需要格式化的数据
            'msg': '获取城市信息成功',
            'status': 200,
            'date': str(time.time()),
            'data': data
        }
        result_fields_dynamic = {   # 数据的格式定制
            'msg': fields.String,
            'status': fields.Integer,
            'date': fields.String,
            'data': fields.Nested(letter_fields_dynamic)
        }

        return marshal(response_data, result_fields_dynamic)