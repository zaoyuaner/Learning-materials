#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author：zhangjiao
'''
函数的重写：
__str__(self),当执行print的时候自动的调用。
'''


import datetime

dtime = datetime.datetime.now()
print(dtime)
print(type(dtime))

class Person():


    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __repr__(self):
        return "%s-%d" % (self.name, self.age)

    # __str__ = __repr__
    # def __str__(self):
    #     return "%s-%d"%(self.name,self.age)

per = Person("lili",18)
print(per)
print(type(per))