#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author：zhangjiao
print()
'''
我们都知道在函数的内部我们可以调用其他的函数，若被调用的这个
函数是他自己本身，这时候我们就称这个函数为递归函数。
【自己调用自己】

递归解决问题的思路：
1.找到临界条件
2.找到这次与上次的关系
3.假设这次的结果已经知道，如何求上次的结果。


递归优点：
定义简单，逻辑清晰
缺点：
1、速度慢
2、对于递归层数有限制，若递归次数过多会造成栈溢出。
在python中，函数调用使用栈进行处理的，每次调用一次函数，则栈增加一层，
函数返回减少一层。
'''

'''
n！ = 1x2x3x...xn
1！= 1
2！= 2x1！
n! = nx(n-1)!
f(n) = nxf(n-1)
'''

# def func():
#     print("hello")
#     return func()

# func()
def f(n):
    if n == 1:
        return 1
    else:
        return n*f(n-1)

print(f(5))
print(f(6))

'''
1+2+3+...+n的和
临界值：n = 1  res = 1
n = n + (n-1)
f(n) = f(n-1)+n 
'''

def func2(n):
    if n==1:
        return 1
    else:
        return n+func2(n-1)


print(func2(10))
print(func2(100))

'''
求斐波那契数列
1、1、2、3、5、8、13、21、34、……
n=1  1
n=2  1
n=3  2
n=(n-1)+(n-2)
f(n) = f(n-1)+f(n-2)
'''

def f2(n):
    if n==1 or n==2:
        return 1
    else:
        return f2(n-1)+f2(n-2)

print(f2(3))
print(f2(4))
print(f2(5))
print(f2(6))