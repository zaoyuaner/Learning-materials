#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author：zhangjiao
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
'''
当子类中有特殊的属性的时候，我们需要手动的调用一下父类中的
构造方法。
在子类中声明变量的时候，无论是继承的属性还是自己特有的属性，
我们都需要自己手动声明。
super().__init__()
'''

class Person:
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex
        print("父类中的构造函数被调用了")

    def eat(self):
        print("吃饭。。。。")

    def sleep(self):
        print("睡觉。。。。")

class Student(Person):
    def __init__(self,name,age,sex,stuId,score):
        # Person.__init__(self,name,age,sex)
        self.stuId = stuId
        self.score = score
        print("子类中的构造函数被调用了")
        # 调用父类的构造方法
        super().__init__(name, age, sex)

    def study(self):
        print("学习。。。")

    def test(self):
        print("考试。。。")


class Teacher(Person):
    def __init__(self,name,age,sex,teaId,stutype):
        super().__init__(name,age,sex)
        self.teaId = teaId
        self.stutype = stutype

    def teach(self):
        print("教学。。。")

    def gaijuan(self):
        print("改卷。。。。")

if __name__ == "__main__":
    stu = Student("lili",18,"girl","1901001",80)
    print(stu.name)
    tea = Teacher("zhangsan",28,"boy","000001","python")
    print(tea.stutype)
    print(tea.name)
    tea.eat()
    tea.gaijuan()
