#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author：zhangjiao
print()
'''
成员变量与类变量（静态成员变量）：

在类中，且在函数体外定义的变量我们通常称为类变量【静态成员变量】，
定义在函数中，并且绑定在self身上的变量，我们称他为成员变量。

什么时候使用类变量?
普通的变量，定义在我们的类中，一般情况下，一些静态这种变量我们可以使用类变量
什么时候使用成员变量？
在创建对象的时候，需要初始化的变量，我们一般情况下都会使用成员变量。
什么使用普通变量？
若此变量只是计算产生的中间变量，后续不需要使用的情况下，
我们可以将其普通变量即可

类变量与成员变量的区别：
1.定义的位置不同，类变量定义在类中并且函数体外，成员变量定义在类的函数中，
并且绑定在self身上
2.出现的时间不同，类变量定义类的时候它就产生了，成员变量实例化对象的时候才生成。
3.调用的方式不同，类变量通过类名来调用【使用对象来调用不报错】
成员变量只能通过对象来进行调用
4.优先级不同，当类变量与成员变量同时存在的时候，使用对象来进行调用，优先去
查找成员变量，若成员变量不存在再查找类变量。

若要更改类变量，我们需要使用类名.变量名来进行更改。
'''
import calendar

class Person:
    PI = 3.1415926
    path = r"E:\python\python1901\day10"
    name = "zhangsan"
    age = 18
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex

    def setMoney(self,mon):
        self.money = mon

    def jisuan(self,n):
        res = 0
        for x in range(n+1):
            res += x
        return res

per = Person("lili",19,"girl")
# per = Person()
# print(per.name)
# print(per.age)
# per.setMoney(10000)
# print(per.money)
# print(Person.sex)
# print(Person.name)
# print(Person.age)

# per.PI = 3.14
print(per.PI)
Person.PI = 3.14

per2 = Person("lili",19,"girl")
print(per2.PI)


