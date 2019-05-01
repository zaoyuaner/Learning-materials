#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author：zhangjiao
'''
什么是函数？
在程序开发的过程中，有些功能需要重复使用，我们会将这些功能进行封装，
在需要使用的时候，调用即可，这段封装的代码，我们称他为函数。
函数的优点：
1.简化代码结构，增强代码的复用性
2.增加代码的可维护性，只需要找到对应的函数，更改里面的代码即可。
'''
'''
定义一个函数：
语法：
def 函数名(参数列表):
    函数体
    return 表达式
    
def代表函数的开始
函数名:遵循标识符的命名规则
参数列表：传入函数的参数，参数与参数之间使用逗号隔开。
函数体：这个函数要实现的功能
return：函数结束之后，返回值，返回值可以是变量、常量也可以是表达式
return可不写，默认为None.
'''
list1 = [1,2,3,45,23]
list1.sort()
print(list1)

'''
定义一个最简单的函数
无参数，无返回值函数

函数的调用：
函数名(参数列表)
'''

def hello():
    for x in range(5):
        print("你好")


def hello2(n):
    for x in range(n):
        print("你好")


def hello3(n,str1):
    for x in range(n):
        print(str1)

# m = int(input("请输入打印的次数："))
# con = input("请输入您要打印的内容：")
# hello3(m,con)

'''
求和：1+2+3+..+n封装一个函数
'''

def qiuhe(n):
    res = 0
    for x in range(1,n+1):
        res += x
    return res

print(qiuhe(10))

def sum(n):
    res = 0
    for i in range(1,n+1):
        res+=i
    return (res)
sum(10)