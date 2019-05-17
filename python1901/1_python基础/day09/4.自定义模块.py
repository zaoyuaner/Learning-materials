#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author：zhangjiao
print()
'''
如何引用自定义模块？
1.整体引入
语法：
import 模块名1[,模块名2,...]
import 模块名2
模块名与模块名使用逗号隔开

函数调用：
模块名.函数名(参数列表)
变量的调用：
模块名.变量名

2.自定义模块之局部引入
from 模块名 import 函数名1/变量名[,函数名2,函数名3...]

函数的调用：
函数名(参数列表)

变量的调用：
变量名

注意：使用这种导入方式，有可能发生变量名或者函数名的冲突。

3.自定义导入之“*”
from 模块名 import *
函数调用：
函数名(参数列表)
变量调用
变量名
注意：一般情况下不建议使用此方法导入，特别容易引起变量名冲突。
'''
import demo
# from collections import Iterable
# from functools import partial
# from day09.demo import hello,height
# from demo import *

# hello("lili")
# print(height)

# def hello():
#     print("你好")
#
# hello("小明")


# demo.hello("小明")
# demo.bye()
#
# print(demo.height)


'''
练习：
求和：1+2+...+n
求阶乘 1x2x...xn
求阶乘之和 1！+2！+..+n!
写成一个模块，并作为自定模块引入
'''