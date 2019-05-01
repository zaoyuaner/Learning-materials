#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author：zhangjiao
print()
'''
在代码运行的期间，我们可以动态的给代码增加功能的方式我们称之为“装饰器”
'''


# print("**************")


def func2():
    print("*************")
    print("2019-2-27")

# func()
# func()

'''
最简单的装饰器：
def outer(func):
    def inner():
        语句块
        return func()
    return inner
函数中嵌套了一个函数，外面的称外函数，里面的称内函数    
外函数参数必须是被装饰式的函数名
在内函数中需要执行被装饰的函数
在外函数返回的时候，需要将内函数的引用【函数名】返回。

注意:
1.外函数的参数被装饰的函数
2.在内函数中一定要执行被装饰的函数
3.外函数的返回值一定是内函数的函数名

调用的时候：
直接将装饰器装饰到被装饰的函数头上
@外函数函数名
def func():  #被装饰函数
    pass 
'''
# func3 = lambda  x,y: x if x>y else y
# func3(2,3)

# func4 = func
# func4()

# def outer(f):
#     def inner():
#         print("**********")
#         return f()
#     return inner


def outer2(func):
    def inner():
        print("**********")
        func()
        print("***********")
        return
    return inner

@outer2
def func():
    print("2019-2-27")



'''
**********
2019-2-27
**********
'''

func()
