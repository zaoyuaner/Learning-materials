#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author：zhangjiao
'''
披萨：
价格：尺寸、
单价：1寸：10块
1.报尺寸--》价格
2.报尺寸--》计算面积
'''
# class Pizza():
#     price = 10
#     def __init__(self,size):
#         self.size = size
#
#     def getPrice(self):
#         return self.price*self.size
#
#     def get_size(self):
#         return (self.size/2)*3.14
#
#
# class Pizza2():
#     price = 10
#
#     # def __init__(self, size):
#     #     self.size = size
#
#     @classmethod
#     def getPrice(cls,size):
#         return cls.price * size
#
#     @staticmethod
#     def get_size(size):
#         return (size / 2)**2 * 3.14
#
#
# if __name__ == "__main__":
#     print(Pizza2.getPrice(10))
#     print(Pizza2.get_size(10))
#
#     # pizza = Pizza(10)
#     # print(pizza.getPrice())
#     #

class Student():
    Pi = 3.1415926

    def sayhello(self):
        print("hello")

stu =Student()
stu.Pi = 3.14
print(Student.Pi)
Student.Pi = 3.14
print(Student.Pi)
