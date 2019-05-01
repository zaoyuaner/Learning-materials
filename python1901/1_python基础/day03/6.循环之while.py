#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author：zhangjiao
print()
'''
求1+2+...+100
'''
'''
while循环语法：
while 判断条件:
    循环体

执行过程：首先进入判断条件，若条件成立，执行循环体，循环体执行完毕之后
继续进行条件判断，若条件依旧成立，则继续执行，循环往复直到条件不成立
的时候退出循环。
'''
n = 1
res = 0  #存储数据
while n<=100: #n = 1     n= 2
    res += n  # res = 0+1  res = 0+1+2
    n += 1    #  n = 2       n=3
print(res)
'''
求1x2x3...x100的积
'''
n = 1
ji = 1
while n<=100:
    ji *= n
    n += 1
print(ji)





