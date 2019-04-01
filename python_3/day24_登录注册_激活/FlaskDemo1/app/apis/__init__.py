from flask_restful import Api

from app.apis.CatApi import CatResource, CatsResource
from app.apis.CityApi import CityResource
from app.apis.GoodsApi import GoodsResource
from app.apis.HelloWorld import HelloResource
from app.apis.LoginApi import Login
from app.apis.RegisterApi import Register

api = Api()

def init_apis(app):
    api.init_app(app)


# 添加资源
api.add_resource(HelloResource, '/api/v1/hello/')


api.add_resource(CatResource, '/api/v1/cat/<int:catid>/')
api.add_resource(CatsResource,'/api/v1/cat/')
api.add_resource(GoodsResource, '/api/v1/goods/')
api.add_resource(CityResource, '/api/v1/city/')
api.add_resource(Register, '/api/v1/register/', endpoint='')
api.add_resource(Login, '/api/v1/login/')