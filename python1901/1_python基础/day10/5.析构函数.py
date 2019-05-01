#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author：zhangjiao
'''
构造函数：实例化对象的时候自动调用
析构函数：释放对象的时候自动调用
析构函数不需要手动调用。
'''
class Student():
    def __init__(self,name,age):
        print("构造函数被调用啦")
        self.name = name
        self.age = age

    def __del__(self):
        print("析构函数被调用啦")

import  time
stu = Student("lili",18)
del stu
time.sleep(3)
