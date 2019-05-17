#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author：zhangjiao
print()
'''
成员方法：
一般在类中定义的方法，大部分都是成员方法。
成员方法能使用对象来进行调用,不能使用类名来进行调用。

静态方法：
就是一类普通的方法，但是写在了类中，使用@staticmethod来进行装饰，
这种方法我们称之为静态方法。
静态方法可以使用类名来进行调用，【推荐使用类名来进行调用】
也可以使用对象来进行调用

类方法：
成员方法是绑定在对象身上的，而类方法绑定类上的方法，使用@classmethod装饰器来进行装饰的方法
专门为类准备的方法，我们称之为类方法。
类方法可以使用对象来进行调用，但是不建议
类方法建议使用类名来进行调用。

什么时候使用类方法？
当写在类中的函数，跟self没关系【没有使用成员变量也没有使用成员方法】，
但是又跟类变量或者类方法有关系【在此函数中，可能使用了类变量或者类方法，静态方法】
这时候我们就可以将这个方法声明成类方法。

什么时候成员方法？
写在类中函数，跟self有关系的时候【使用了成员变量或者成员方法】，
这时候我们必须要将此方法写成成员方法。

什么使用静态方法？
写在类中的函数，既跟self没没关系，跟类也没关系【没有使用成员变量、也没使用类变量
没有使用类方法、没有使用成员方法、静态方法也没使用】，此时我们就可以将此方法
写成静态方法。

'''

'''
总结：
1.成员方法隐含参数self，类方法的隐含参数cls、静态方法没有隐含参数
2.成员方法、静态方法、类方法都是使用对象来进行调用，成员方法不能使用类名来进行调用
3.静态方法与类方法虽然能够使用对象调用，但是不建议使用。
【因为静态方法与类方法是专门给类准备的。】
'''
from datetime import datetime


class Music():
    index = 0
    def __init__(self,name):
        self.name = name

    def play(self):
        print("play music",self.name)


    @staticmethod
    def welcome():
        print("欢迎光临。。。")

    @classmethod
    def getNext(cls):
        print(cls)
        cls.index += 1
        print("下一曲index为",cls.index)



if __name__=="__main__":
    # print(datetime.now())
    # print(datetime(2019, 3, 8).now())
    # Music.play()
    music = Music('huh')
    music.welcome()
    print(type(music))
    music.getNext()
    Music.getNext()

