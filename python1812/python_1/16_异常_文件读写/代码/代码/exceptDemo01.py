#一、try-except-else的使用

#1.except带有异常类型
try:
    print(10 / 0)
except ZeroDivisionError as e:
    print("被除数不能为0",e)

print("~~~~")
"""
总结：
a.try-except屏蔽了异常，保证后面的代码可以正常执行
b.except ZeroDivisionError as e相当于声明了一个ZeroDivisionError类型的变量【对象】，变量e中携带了错误的信息
"""

#2.try后面的except语句可以有多个
class Person(object):
    __slots__ = ("name")
try:
    p = Person()
    p.age = 19

    print(10 / 0)
except AttributeError as e:
    print("属性异常",e)
except ZeroDivisionError as e:
    print("被除数不能为0",e)

print("over")

"""
总结：
a.一个try语句后面可以有多个except分支
b.不管try中的代码有多少个异常，except语句都只会被执行其中的一个，哪个异常处于try语句的前面，则先先执行对应的except语句
c.后面的异常不会报错【未被执行到】
"""

#3.except语句的后面可以不跟异常类型
try:
    print(10 / 0)
except:
    print("被除数不能为0")


#4.一个except语句的后面可以跟多种异常的类型
#注意：不同的异常类型使用元组表示
try:
    print(10 / 0)
except (ZeroDivisionError,AttributeError):
    print("出现了异常")


#5.else分支
try:
    print(10 / 4)
except ZeroDivisionError as e:
    print("出现了异常",e)
else:
    print("hello")

"""
总结：
a.如果try中的代码出现了 异常，则直接去匹配exceptelse分支不会被执行
b.如果try中的代码没有出现异常，则try中的代码正常执行，except不会被执行，else分支才会被执行
"""

#6.try中不仅可以直接处理异常，还可以处理一个函数中的异常
def show():
    x = 1 / 0

try:
    show()
except:
    print("出现了异常")

#7.直接使用BaseException代替所有的异常
try:
    y = 10 / 0
except BaseException as e:
    print(e)

"""
总结：在Python中，所有的异常其实都是类，他们都有一个共同的父类BaseException，可以使用BaseException将所有异常“一网打尽”
"""
