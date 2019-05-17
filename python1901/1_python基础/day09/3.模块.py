#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author：zhangjiao
print()
'''
模块的定义：
在python中一个.py文件我们称之为一个模块。
模块划分：按照功能来进行划分，相同或者相似的我们将其放到一个模块中去。

优点：
1、提高代码的可维护性
2、提高代码的复用性
3、可以引入其他模块
4、可以避免函数名与变量名的冲突
'''

import math


def pow(a,b):
    return a+b

print(math.pow(2,3))
print(pow(2,3))