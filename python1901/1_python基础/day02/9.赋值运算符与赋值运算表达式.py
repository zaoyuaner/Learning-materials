#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author：zhangjiao
print()
'''
赋值运算符：=
赋值运算表达式
+=  a = a+b
-=   a = a-b
*=   a = a*b
/=   a = a/b
%=    a = a%b
**=   a = a**b
//=   a = a//b

写在等号左边的变量会发生变化，表达式计算结束之后给其进行重新赋值
写在等号右边的只是参与运算，它的值不发生变化。
'''
n = 0
n += 1
b = 20
a = 10
a += b
print(a)  # 30
print(b)  #20

a -= b
print(a)  # 10
print(b)  #20

a *= b
print(a)  # 200
print(b)  #20

a /= b
print(a)  #10
print(b)  #20


a %= b
print(a) #10
print(b) #20

a **= b
print(a) #10^20
print(b) #20

a //= b
print(a) #10^20/20
print(b) #20