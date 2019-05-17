from flask_restful import Api

from app.apis.GoodsAPI import GoodsResource
from app.apis.RegisterAPI import RegisterResource
from app.apis.WheelApi import WheelResource

api = Api()

def init_api(app):
    api.init_app(app)

#添加资源
api.add_resource(WheelResource,'/wheel/')
api.add_resource(GoodsResource,'/goods/')
api.add_resource(RegisterResource,'/api/register/')


