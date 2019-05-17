#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author：zhangjiao
'''
一个子类可以继承多个父类，比如一个孩子，有一个爸爸，有一个妈妈
多继承：
1.若同时继承多个父类的时候，需要手动初始化父类构造函数
2.当父类中的函数名出现相同的时候，优先选择写在继承元组前面的那个。
子类与父类的关系：
一个子类可以有多个父类，一个父类也可以有多个子类。
'''
class Father():
    def __init__(self,name,money):
        self.name = name
        self.money = money

    def sing(self):
        print("两只老虎跑的快。。。")

    def eat(self):
        print("吃肉。。。。")


class  Mother():
    def __init__(self,name,faceValue):
        self.name = name
        self.faceValue = faceValue

    def dance(self):
        print("广场舞。。。。")

    def eat(self):
        print("吃水果。。。。")

class child(Father,Mother):
    def __init__(self,name,money,faceValue):
        Father.__init__(self,name,money)
        Mother.__init__(self,name,faceValue)



if __name__ == "__main__":
    child = child("xiaoming",10000000,95)
    print(child.name)
    print(child.faceValue)
    print(child.money)
    child.dance()
    child.sing()
    child.eat()
