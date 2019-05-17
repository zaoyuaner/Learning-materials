#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author：zhangjiao
print()
'''
面向对象三大特征：
封装、继承、多态【鸭子模型】
封装是什么？
广义的封装：函数、模块、类就是封装的体现
狭义的封装：变量私有化的过程。

封装的优点：
1.调用方便
2.可以对数据进行过滤处理

@property 这个装饰器它可以将一个方法变成属性来进行调用。
当我们使用@property的时候，它又会生成一个@属性.setter的装饰器
这个装饰器可以将设置的函数变成属性来进行调用
使用此装饰器，可以使我们的调用更加简单，同时还可以添加一些必要的数据
过滤
'''


class Person():
    def __init__(self,name,age,money):
        self.name = name
        self.__age = age
        self.__money = money


    @property
    def money(self):
        return self.__money

    @money.setter
    def money(self,mon):
        if mon>0:
            self.__money += mon
        else:
            print("金额非法。。。")




    # def setAge(self,age):
    #     if age>=0 and age<=180:
    #         self.__age = age
    #     else:
    #         print("年龄非法")
    #         return

    # def getAge(self):
    #     return self.__age
    @property  #相当于getter的方法，获取
    def age(self):
        return self.__age

    @age.setter  #相当于setter的方法，设置
    def age(self,age):
        if age >= 0 and age <= 180:
            self.__age = age
        else:
            print("年龄非法")
            return



'''
需求：将age私有化，并且设置age取值范围[0,180]
'''

if __name__ == "__main__":
    per = Person("lili",18,100000)
    # print(per.name)
    # print(per.age)
    # print(per.__money)
    # per.setMoney(50)
    # print(per.getMoney())

    # per.setAge(-10)
    # # per.setAge(10)
    # print(per.getAge())

    per.age = -10
    print(per.age)
    per.money = -100
    print(per.money)