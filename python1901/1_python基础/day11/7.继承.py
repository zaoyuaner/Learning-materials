#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author：zhangjiao
print()
'''
继承：
如果两个或者两个以上的类具有一些相同的属性或者方法，我们可以
将相同的属性或者方法抽取出来，这个抽取出来的类我们叫做父类/超类/基类
其他的类我们子类/派生类，他们之间的关系就是继承。
注意：若一个类没有继承任何类，默认情况下继承object类，
1、object类是一切类的基类
2、子类对象可以访问父类中除了被私有化的所有的属性以及方法。
3.父类不能访问子类特有的方法以及属性
继承的优点：
1.提高代码的可维护性
2.提高代码的复用性
3.提高代码的安全性
缺点:增加代码的耦合度。
'''
'''
创建一个基类：人类
创建一个
学生类
属性：学号、姓名、班级、年龄、性别、分数
行为：学习、考试、吃饭、睡觉
、与老师类
属性：工号、姓名、年龄、性别、学科
行为：教学、改卷、吃饭、睡觉
学生类与老师类具有自己特有的方法与属性
'''
# class Person:
#     pass
# class Person():
#     pass
# class Person(object):
#     pass



class Animal:

    def __init__(self,name,age,pinzhong,color):
        self.name = name
        self.age = age
        self.pinzhong = pinzhong
        self.__color = color

    def eat(self,food):
        print("%s吃%s"%(self.name,food))

    def run(self):
        print("%s跑。。。。。"%self.name)

class Cat(Animal):
    def catchMouse(self):
        print("%s抓老鼠"%self.name)

class Dog(Animal):
    pass

if __name__ == "__main__":
    cat = Cat("tom",2,"波斯猫","白色")
    cat.eat("老鼠")
    cat.catchMouse()

    # ani = Animal("ani",3,"杂交","黄色")
    # ani.catchMouse()
    # dog = Dog("jerry",1,"泰迪","灰色")
    # dog.run()



