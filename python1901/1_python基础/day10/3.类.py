#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author：zhangjiao
print()
'''
类的设计：
1.类名： 人类  person
2.特征：身高、体重、姓名、年龄、性别 【名词】
3.行为：吃饭、跑步、睡觉、唱歌 【动词】
'''
'''
在类中定义方法以及属性：
1.定义类名
2.特征 《---->属性
3.行为  《===========》方法/函数

在class内部定义的一般的函数，我们称之为成员方法，
成员的第一个参数是self，self代表对象本身，不需要我们手动传递。
'''
class Person:
    height = 180
    weight = 80
    name = "xiaonming"
    age = 20
    sex = "boy"

    def eat(self):
        # print(self)
        print("吃饭。。。。。")

    def run(self):
        print("跑步。。。。")

    def sleep(self):
        print("睡觉。。。。")


    def sing(self):
        print("唱歌。。。。")

per = Person()
per.eat()


'''
如何使用类？
实例化对象：
对象名 = 类名()
如何使用类中的方法与属性： 
对象名.属性
对象名.方法名(参数列表)

在对象中更改类中的属性的时候，只更改当前对象，其他对象不受影响。

'''
# per = Person()
# print(per.name)
# print(per.height)
# print(per)
# per.eat()
# per.run()
#
per1 = Person()
# print(per1.name)
# print(per is per1)
# set1 = set()
# print(type(set1))

per1.name = "lili"
per1.height = 160
per1.weight = 50

print(per1.name)
print(per1.height)
print(per1.weight)

per2 = Person()
print(per2.name)


'''
需求：创建一个学生类：
1.类名
2.特征：姓名、年龄、性别、学号、成绩
3.行为：学习、吃饭、睡觉、自我介绍
'''

class Student():
    name = "lili"
    age = 18
    sex = "girl"
    studentId = "1901001"
    score = 0

    def study(self):
        print("学习。。。。")

    def eat(self,food):
        print("吃%s"%food)


    def sleep(self):
        print("睡觉。。。。")

    def ins(self):
        print("我是%s，我今年%d岁，我的学号是%s"%(self.name,self.age,self.studentId))



# stu = Student()
# stu.ins()
# stu.eat("饺子")
# stu.name = "xiaoming"
# stu.age = 19

'''
创建一个类，模仿calendar，
实现两个方法，第一个判断是否为闰年
第二个，两个年份之间有多个闰年。
'''

class calendardemo:

    def isleap(self,year):
        if year%4==0 and year%100!=0 or year%400 == 0:
            return  True
        else:
            return False


    def leapdays(self,year1,year2):
        count = 0
        for x in range(year1,year2):
            if self.isleap(x):
                count += 1
        return count


# cal = calendardemo()
# print(cal.isleap(2018))
# print(cal.isleap(2020))
# print(cal.isleap(200))
# print(cal.leapdays(2018,2030))










