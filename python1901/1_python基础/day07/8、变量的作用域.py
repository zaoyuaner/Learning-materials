#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author：zhangjiao
print()
'''
变量的作用域：
变量的作用域就是指的是变量的可使用范围。
'''

'''
局部作用域【在def中包含的作用域】：
局部变量：定义在def/lambda关键字中的，换句话说，在函数体中定义
的变量，它的作用域就是当前函数，当函数执行结束之后，这个
变量所占用的内存就会被回收。

嵌套作用域：
在嵌套函数中外函数中的作用域

全局作用域：
在全局作用域中定义的变量，我们称他为全局变量。
全局变量指的是定义在.py文件内，函数体【类体】外的变量。
整个.py文件中都能使用

内置作用域：
系统内部固定的变量
使用范围，整个python项目中都可以使用。

变量名的解析法则：
搜索的优先级：
局部作用域>嵌套作用域>全局作用域>内置作用域

若在函数体内要更改全局变量的时候，需要使用global关键字
声明此变量为全局变量，再进行更改。

什么时候会产生新的作用域？
在python中只有模块、类（class）、函数（def/lambda）才会产生
新的作用域，而if/else、try/except、while、for这些语句块
不会产生新的作用域。
#产生新的作用域：
'''

# for i in range(20):
#     # print(i)
#     pass
# print(i)
# print(vars())
# print(__name__)
num = 20
# def outer():
#     num = 10
#     print("outer",num)
#     def inner():
#         num = 100
#         print("inner",num)
#     return inner
# outer()()
num2 = 3000


# print(id(num))
def func():
    global num
    num = 10

func()
print(num)
#
# func()
# print(num)