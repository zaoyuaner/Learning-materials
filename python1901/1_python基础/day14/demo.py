#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author：zhangjiao

def sum1(a,b):
    return a+b

def jiecheng(n):
    res = 1
    for x in range(1,n+1):
        res *= x
    return res


class Person():
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def getAge(self):
        return self.age+1