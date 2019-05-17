## 一、REST
REST是"Representational State Transfer"缩写，即是"表现层状态转化"。而"表现层"其实指的是"资源(Resource)"的表现层。
```
表现层: 资源(例如图片、歌曲、用户....)
状态转换:  GET获取、POST添加、DELETE删除、PUT更新...
```

## 二、视图
```
- FBV 视图函数
	Function base view基于函数的视图

- CBV 类视图
	Class base view基于类的视图
```


## 三、DRF基础
- 文档
    ```
    https://www.django-rest-framework.org/
    https://q1mi.github.io/Django-REST-framework-documentation/
    ```

- 模型定义
    ```
    class Book(models.Model):
        name = models.CharField(max_length=100)
        price = models.IntegerField()
    ```

- 序列化
    ```
    from rest_framework import serializers
    from app3.models import Book

    # serializers.Serializer 原始序列化，手动序列化
    # serializers.ModelSerializer 序列化模型(最常用)
    # serializers.HyperlinkedModelSerializer 序列化模型，添加一个超链接
    class BookSerializer(serializers.ModelSerializer):
        class Meta:
            model = Book
            fields = ('name', 'price', 'id')
    ```

- 类视图
    ```
    class BookAPIView(APIView):
        def post(self, request):     # 添加数据
            # 客户端的请求的数据 request.data
            serializer = BookSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)


            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        def get(self, request): # 获取所有数据
            books = Book.objects.all()
            serializer = BookSerializer(books, many=True)
            return Response(serializer.data)
    ```
    > APIView其实是继承Django中View!


- 路由
    ```
    urlpatterns = [
        url(r'^book/$', views.BookAPIView.as_view()),
    ]
    ```

## 四、基于mixins
- 概述
    ```
    CreateModelMixin: 创建模型
    ListModelMixin: 获取结果集
    RetrieveModelMixin: 检索
    UpdateModelMixin: 更新
    DestroyModelMixin: 删除
    ```

- 基本操作
    ```
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
    ```

## 五、基于generic
- 概述
    ```
    CreateAPIView: 创建模型 的类视图
    ListAPIView: 获取结果 的类视图
    RetrieveAPIView: 检索 的类视图
    DestroyAPIView: 删除 的类视图
    UpdateAPIView: 更新 的类视图
    ListCreateAPIView: 创建、获取结果集 的类视图
    RetrieveUpdateAPIView: 检索、更新 的类视图
    RetrieveDestroyAPIView: 检索、删除 的类视图
    RetrieveUpdateDestroyAPIView: 检索、更新、删除 的类视图
    ```
    > Update包含put和patch请求方法。put更新整个，patch局部更新。