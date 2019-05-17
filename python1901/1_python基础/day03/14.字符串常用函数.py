#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author：zhangjiao
print()
'''
eval(str1)
功能:将字符串转为有效的表达式并且返回计算的结果.

len(str1)
功能:返回字符的长度.

str1.lower()
功能:将字符串中所有的大写字母转为小写字母

str1.upper()
功能:将字符串中所有的小写字母转为大写字母

str1.swapcase()
功能:将字符串中的大写字母转成小写,将小写字母转为大写.

str1.capitalize()
功能:将字符串中的第一个字符转为大写,其他都小写

str1.title()
功能:将字符串中的每个单词首字母大写,其他都小写.
'''
print((eval("12+3")))
print(type(eval("12.34+3")))
print((eval("[1,2,3,4]")))

# print(len("1223"))
# print("HEllo".lower())
# print("HEllo".upper())
# print("HEllo".swapcase())
# print("HEllo World".capitalize())
# print("HEllo world USA".title())
str1="123efs"
print(str1.upper())
