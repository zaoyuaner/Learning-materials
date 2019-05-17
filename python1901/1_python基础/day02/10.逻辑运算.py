#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author：zhangjiao
print()
'''
逻辑运算
and  与运算  使用and连接的只有结果都为True的时候，它的结果才为True
or  或运算   使用or连接的，只要有一个条件满足，它的结果就为True。 
not  非运算  单目运算，真变假，假变真

短路原则：
当我们使用and连接的时候，只要有一个表达式是假的，后面的表达式则不再进行
计算，直接返回False。
当我们使用or连接的时候，只要有一个表达式为真，后面的表达式则不再进行计算
，直接返回True。
'''
print(not False)
print(not True)

# print(True or False)
# print(False or False)
# print(True or True)

# print(True and False)
# print(False and False)
# print(True and True)

'''
小括号优先级>not优先级最高>and优先级>or优先级
'''

