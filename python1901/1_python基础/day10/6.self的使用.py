#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author：zhangjiao
'''
self是关键字么？
self不是一个关键字，用其他的名字代替是可以的，但是一般情况下建议使用self
这个约定熟成的写法。
1.当我们声明函数的时候，self必须要声明
2.函数调用的时候，不需要手动传递此参数，它会自动传递。
'''

class  Student():

    def __init__(self,name,age):
        print("self",self)
        self.name = name
        self.age = age


    def ins(s):
        print("s",s)
        print("我的名字叫%s，我今年%d岁"%(s.name,s.age))


stu = Student("lili",18)
stu.ins()

'''
需求：同桌买了一部华为mateX跟你炫耀.（17000）
人类：
属性：name，age、手机，money
行为：炫耀

手机类：
属性：品牌、型号、价格
行为：折叠、双面拍照
'''



