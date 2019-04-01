from flask_restful import Resource,fields, marshal_with
from app.models import Cat


# 返回一只猫
# class CatResource(Resource):
#     def get(self, catid):
#         # cat = Cat.query.first()
#         cat = Cat.query.get(catid)
#
#         response_data = {
#             'count': 1,
#             'msg': '获取数据成功',
#             'subject': {    # 猫的信息
#                 'id': cat.id,
#                 'name': cat.name,
#                 'color': cat.color,
#                 'age': cat.age
#             }
#         }
#
#         return response_data


""" 需要返回的数据示例
{
    'msg': '获取一只猫信息成功',
    'count': 1,
    'data': {
        'id': 1,
        'name': '大花猫',
        'age': 3,
        'color': '白色'
    }
}
"""

# 响应格式定制
cat_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'age': fields.Integer,
    'color': fields.String
}

result_fileds = {
    'msg': fields.String,
    'count': fields.Integer,
    'data': fields.Nested(cat_fields),
    'err': fields.String
}

class CatResource(Resource):
    @marshal_with(result_fileds)
    def get(self, catid):
        cat = Cat.query.get(catid)

        response_data = {
            'count': 1,
            'msg': '获取数据成功',
            'data': cat,
        }

        return response_data



# 返回多只
# class CatsResource(Resource):
#     def get(self):
#         cats = Cat.query.all()
#
#         response_data = {
#             'count': 1,
#             'msg': '获取数据成功',
#             'subject': [
#                 {  # 猫的信息
#                     'id': cats[0].id,
#                     'name': cats[0].name,
#                     'color': cats[0].color,
#                     'age': cats[0].age
#                 },
#                 {  # 猫的信息
#                     'id': cats[1].id,
#                     'name': cats[1].name,
#                     'color': cats[1].color,
#                     'age': cats[1].age
#                 },
#                 {  # 猫的信息
#                     'id': cats[2].id,
#                     'name': cats[2].name,
#                     'color': cats[2].color,
#                     'age': cats[2].age
#                 },
#                 {  # 猫的信息
#                     'id': cats[3].id,
#                     'name': cats[3].name,
#                     'color': cats[3].color,
#                     'age': cats[3].age
#                 },
#             ],
#         }
#
#         return response_data



''' 返回数据示例
{
    'message': '返回数据成功',
    'status': 200,
    'total': 2,
    'data': [
        {   # 一只猫
            'id': 1,
            'name': '大花猫',
            'color': '花色',
            'age': 4
        },
        {   # 一只猫
            'id': 1,
            'name': '大花猫',
            'color': '花色',
            'age': 4
        },
    ]
}
'''

resource_fields = {
    'message': fields.String,
    'status': fields.Integer,
    'total': fields.Integer,
    'data': fields.List(fields.Nested(cat_fields))
}

class CatsResource(Resource):
    @marshal_with(resource_fields)
    def get(self):
        cats = Cat.query.all()

        response_data = {
            'message': '获取猫的信息成功',
            'status': 200,
            'total': len(cats),
            'data': cats
        }

        return response_data