#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author：zhangjiao
num1 = "1233"
num2 = "I"
num3 = "一"
num4 = "壹二"
# print(num1.isdigit())  #只识别阿拉伯数字
# print(num2.isdigit())
# print(num3.isdigit())


# print(num1.isnumeric())  #中文可以识别
# print(num2.isnumeric())
# print(num3.isnumeric())
# print(num4.isnumeric())

print(num1.isdecimal())  #只识别阿拉伯数字
print(num2.isdecimal())
print(num3.isdecimal())
print(num4.isdecimal())
