#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author：zhangjiao
'''
参数传递的本质：实参给形参赋值的过程。
'''

'''
位置参数，【又称必选参数】
位置参数传参的时候，传递顺序是不可变的。

关键字传参：使用键值对的方式来进行传参的
1.数据更加清晰
2.可以清除位置关系
注意：键--》形参名

当位置参数与关键字参数同时存在的时候，我们需要将位置参数
写在关键字参数的前面。

默认参数：
定义函数的过程中，我们可以给参数设置默认值，调用函数的时候
我们可以传递该参数，也可以不传递，当传递该参数的时候，我们使用
传递的参数，若不传递该参数，则使用默认参数。
好处：方便我们的调用。

在定义的时候，当必选参数与默认参数同时存在的时候，我们需要将
默认参数写在必选参数的后面。
'''

def func(name,age,address):
    print("我的名字叫%s，我今年%d岁,我家住在%s"%(name,age,address))


def func2(name,age,address="江西"):
    print("我的名字叫%s，我今年%d岁,我家住在%s"%(name,age,address))


def func2(age,name="小明",address="江西"):
    print("我的名字叫%s，我今年%d岁,我家住在%s"%(name,age,address))

# def func2(aa,bb):
#     print("我的名字叫%s，我今年%d岁"%(aa,bb))
func("张三",20,"东北")
func(address="深圳",age=20,name="lili")
func("xiaoming",address="上海",age=18)

# print("*****",end="\t")
# print("*****",end="\t")
func2("xiaohong",18)
func2("小华",20,"上海")

list1 = [1,3,34,5]
# list1.sort(reverse=False)
