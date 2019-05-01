#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author：zhangjiao
'''
1.前后双下划线 比如__func__,一般是系统定义的函数或者变量
2.首双下划线  __func ,代表私有化的，不能直接访问。
3.首单下划线 _func,代表保护类型的，虽然它可以直接被访问，
但是请把它视为私有变量，不要直接访问。


'''



class Person:
    __slots__ = ("name","__age__","_money")

    def __init__(self,name,age,money):
        self.name =name
        self.__age__ = age
        self._money = money


if __name__ == "__main__":
    per = Person("lili",18,1000)
    print(per.__age__)
    print(per._money)
