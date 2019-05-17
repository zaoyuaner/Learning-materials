
from rest_framework import mixins, viewsets
from rest_framework.decorators import list_route
from django.core.cache import cache
from rest_framework.response import Response

from carts.models import Cart
from carts.serialziers import CartSerializer
from utils.UserAuthentication import UserAuth


class CartView(viewsets.GenericViewSet,
               mixins.ListModelMixin,
               mixins.UpdateModelMixin):

    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    # 认证class
    authentication_classes = (UserAuth,)

    def list(self, request, *args, **kwargs):
        # {code:200, msg:'', data: {carts:'', total_price:''}}
        # carts : { id: '', c_goods: {id:12, img: '//...'}  }
        queryset = self.get_queryset()
        # 过滤出当前登录系统用户的购物车信息
        queryset = queryset.filter(c_user=request.user)
        serializer = self.get_serializer(queryset, many=True)

        # 计算总价
        queryset = queryset.filter(c_is_select=1).all()
        total_price = 0
        for cart in queryset:
            total_price += cart.c_goods.price * cart.c_goods_num

        res = {
            'carts': serializer.data,
            'total_price': total_price
        }
        return Response(res)



    @list_route(methods=['POST'])
    def add_cart(self, request, *args, **kwargs):
        goodsid = request.data.get('goodsid')
        # 如果当前登录系统用户已添加同一商品，则商品数量加一
        cart = Cart.objects.filter(c_user=request.user,
                                   c_goods_id=goodsid).first()
        if not cart:
            # 购物车中没有该账号添加的对应商品信息
            Cart.objects.create(c_user=request.user,
                                c_goods_id=goodsid)
        else:
            # 购物车中有该账号添加的该商品信息
            cart.c_goods_num += 1
            cart.save()
        res = {
            'code': 200,
            'msg': '添加成功'
        }
        return Response(res)


    @list_route(methods=['POST'])
    def sub_cart(self, request, *args, **kwargs):
        user = request.user
        goodsid = request.data.get('goodsid')
        carts = Cart.objects.filter(c_user=user, c_goods_id=goodsid).first()
        res = {'code': 200, 'msg': '操作成功'}
        if not carts:
            # 购物车中没有该商品的信息
            res = {'code': 1008, 'msg': '购物车中没有该商品，无法完成该操作'}
        if carts.c_goods_num > 1:
            # 更新，减少商品的数量，减一操作
            carts.c_goods_num -= 1
            carts.save()
        else:
            # 当商品的数量为1的时候，删除商品信息
            carts.delete()
        return Response(res)


    # @list_route(methods=['POST'])
    # def add_cart(self, request, *args, **kwargs):
    #     # 思路: 登录和没登录情况
    #     # 1. 登录信息的判断，cache使用
    #     token = request.data.get('token')
    #     goodsid = request.data.get('goodsid')
    #     user_id = cache.get(token)
    #     if user_id:
    #         # 2. 如果当前登录系统用户已添加同一商品，则商品数量加一
    #         cart = Cart.objects.filter(c_user_id=user_id,
    #                                    c_goods_id=goodsid).first()
    #         if not cart:
    #             # 购物车中没有该账号添加的对应商品信息
    #             Cart.objects.create(c_user_id=user_id,
    #                                 c_goods_id=goodsid)
    #         else:
    #             # 购物车中有该账号添加的该商品信息
    #             cart.c_goods_num += 1
    #             cart.save()
    #         res = {
    #             'code': 200,
    #             'msg': '添加成功'
    #         }
    #     # 3. 没有登录，直接返回状态码
    #     else:
    #         res = {
    #             'code': 1007,
    #             'msg': '用户没有登录，请先登录，再操作'
    #         }
    #     return Response(res)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.c_is_select = not instance.c_is_select
        instance.save()
        res = {
            'code': 200,
            'msg': '修改成功'
        }
        return Response(res)

    @list_route(methods=['PATCH'])
    def change_select(self, request, *args, **kwargs):
        # 修改当前登录用户的购物车中的商品的所有选择状态
        user = request.user
        Cart.objects.filter(c_user=user).update(c_is_select=1)
        res = {
            'code': 200,
            'msg': '请求成功'
        }
        return Response(res)