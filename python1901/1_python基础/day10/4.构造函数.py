#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author：zhangjiao
'''
构造函数/方法：
__init__(self)这个函数不需要手动调用，当我们创建对象的时候
会自动的调用此方法。构造函数初始化对象。
与普通函数相比，构造函数不同点：
1.函数名是固定，不能更改的
2.构造函数是不需要手动调用的，实例化对象的时候，自动调用的
'''

'''
需求：创建一个学生类：
1.类名
2.特征：姓名、年龄、性别、学号、成绩
3.行为：学习、吃饭、睡觉、自我介绍
'''

class Student():

    def __init__(self,name,age,sex,studentId,score):
        # print("构造函数")
        # print(name,age,sex,studentId,score)
        self.name = name
        self.age = age
        self.sex = sex
        self.studentId = studentId
        self.score = score

stu = Student("lili",19,"girl","1901002",80)
stu2 = Student("lili",19,"girl","1901002",80)
# print(stu.name)
print(id(stu))
print(id(stu2))
stu3 = stu
print(id(stu3))
stu3.__demo__()
