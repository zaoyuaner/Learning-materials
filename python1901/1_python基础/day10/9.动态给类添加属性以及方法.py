#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author：zhangjiao
print()
'''
我们可以动态的给我们的对象绑定属性以及方法，但是需要注意，
给对象动态绑定的属性和方法，只作用于当前对象，对其他对象不起作用。

但是，动态给类绑定的属性或者方法，作用于类中所有的对象。

有时候，我们不想随意给我们的对象添加一些属性的时候，我们可以使用
__slots__属性，这个属性它是一个元组，我们将可以添加的属性的属性名
一一列举，写到元组中。
使用slots设置的类只对当前类的实例起作用，对子类不起作用。
'''
class Student:
    pass

# stu = Student()
# stu.name = "lili"
# stu.age = 18
#
def sayhello():
    print("hello")
#
# stu.hello = sayhello
#
# print(stu.name)
# print(stu.age)

stu.hello()
#
# stu2 = Student()
# stu2.hello()

# Student.name = "小明"
# Student.age = 19
# Student.hello = sayhello
#
# stu3 = Student()
# print(stu3.name)
# print(stu3.age)

#
# class Student:
#     __slots__ = ("name","age","sex","studentId")
#     def __init__(self,name,age,sex,studentId):
#         self.name = name
#         self.age = age
#         self.sex = sex
#         self.studentId = studentId
#
#
# stu = Student("lili",18,"girl","1901003")
# print(stu.name)
# print(stu.age)
# # stu.score = 80
# # print(stu.score)
#
# stu.name= "xiaoming"
# print(stu.name)


