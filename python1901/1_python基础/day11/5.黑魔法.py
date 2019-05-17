#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author：zhangjiao
'''
黑魔法：
被私有化的属性是不是一定不能直接访问呢？
被私有化的属性不能直接访问的原因是，python解释器解释被私有化的属性的时候
解释成，_类名__属性名，当我们直接访问的时候就会出错。但是我们通过python解释器
解释的_类名__属性名 来进行访问，但是在python强烈不建议这么干，因为不同的解释器
解释出来的变量名可能不同。
'''

class Person():
    def __init__(self,name,age):
        self.name = name
        self.__age = age


if __name__ == "__main__":
    per = Person("lili",18)
    print(per._Person__age)
    per._Person__age = 20
    print(per._Person__age)
