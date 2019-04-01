from flask_restful import Resource,reqparse, fields, marshal_with


# 请求格式定制
parser = reqparse.RequestParser()
# 参数可选
# parser.add_argument('page', type=int, help='请提供页码page')
# parser.add_argument('per', type=int, help='请提供当前页显示记录数据量per')

# 必填
parser.add_argument('page', type=int, required=True,help='请提供页码page')
parser.add_argument('per', type=int, required=True,help='请提供当前页显示记录数据量per')


# 响应格式定制
result_fields = {
    'msg': fields.String,
}

class GoodsResource(Resource):
    @marshal_with(result_fields)
    def get(self):
        parse = parser.parse_args()
        page = parse.get('page') or 1
        per = parse.get('per') or 5

        return {'msg':'GET请求参数设置第{}页-{}'.format(page,per)}

    @marshal_with(result_fields)
    def post(self):
        parse = parser.parse_args()
        page = parse.get('page') or 1
        per = parse.get('per') or 5

        return {'msg': 'POST请求参数设置第{}页-{}'.format(page, per)}