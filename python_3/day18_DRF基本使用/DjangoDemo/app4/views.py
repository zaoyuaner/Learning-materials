from django.shortcuts import render
from rest_framework import mixins, generics
from app4.models import News
from app4.serializers import NewsSerializer


class NewsAPIView(
    mixins.CreateModelMixin,    # 继承后，就有创建的方法
    mixins.ListModelMixin,      # 继承后，就有获取列表方法
    generics.GenericAPIView     # 继承后，就是类视图
):    # 添加新闻、获取新闻列表
    queryset = News.objects.all()
    serializer_class = NewsSerializer

    def post(self, request, *args, **kwargs):   # 添加数据
        return self.create(request, *args, **kwargs)


    def get(self, requeset, *args, **kwargs):   # 获取列表
        return self.list(requeset, *args, **kwargs)


class NewsDetailAPIView(
    generics.GenericAPIView,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

    def get(self, request, *args, **kwargs):    # 获取单个
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):    # 更新数据
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs): # 删除数据
        return self.destroy(request, *args, **kwargs)
