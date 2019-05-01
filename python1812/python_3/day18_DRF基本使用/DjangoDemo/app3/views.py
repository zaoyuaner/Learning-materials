from django.http import Http404
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from app3.models import Book
from app3.serializers import BookSerializer


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


# 单个数据操作
class BookDetail(APIView):
    def get_obj(self, pk):
        try:
            return Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            raise Http404

    def get(self, request, pk): # 获取单个数据
        book = self.get_obj(pk)

        serializer = BookSerializer(book)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):  # 删除数据
        book = self.get_obj(pk)
        book.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk): # 更新数据
        book = self.get_obj(pk)
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_202_ACCEPTED)

        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
