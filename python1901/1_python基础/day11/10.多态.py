#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author：zhangjiao
'''
多态本身基于继承：
 “当看到一只鸟走起来像鸭子、游泳起来像鸭子、叫起来也像鸭子，
 那么这只鸟就可以被称为鸭子。”---鸭子模型
 在鸭子类型中，关注的不是对象的类型本身，而是它是如何使用的。
自定义的class就是自定义的一种数据类型.
猫是动物，狗是动物
动物：多种表现形态：
序列：list/tuple/dict 多种表现形态
一种事务具有多种表现形态，我们称之为多态【依赖于继承的】
python是一门动态数据类型的语言

python的鸭子模型优点：
1.增加代码的灵活性
2.不关注我们的数据类型，关注使用的方法

在python中并不存在真正意义上的多态，原因python是动态数据类型的语言
传入什么类型，接收什么样的类型。
'''

class Animal:

    def __init__(self,name):
        self.name = name

    @classmethod
    def run(cls,obj):
        if not isinstance(obj,Animal):
            print("类型不对")
            return
        obj.run()


class Person():
    def run(self):
        print("人跑的快...")


class Cat(Animal):

    def run(self):
        print("cat 跑得快")

class Dog(Animal):

    def run(self):
        print("dog跑的快")

if __name__ == "__main__":
    cat = Cat("tom")
    # cat.run()
    Animal.run(cat)
    dog = Dog("jerry")
    # dog.run()

    per = Person()
    Animal.run(per)

    print(isinstance(cat,Animal))
    print(isinstance(dog,Animal))
    print(isinstance(per,Animal))

