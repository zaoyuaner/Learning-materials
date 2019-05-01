#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author：zhangjiao

from io import StringIO


#创建了stringio的对象
str1 = StringIO()
#向stringio写入字符串
str1.write("hello")
str1.write("world")
#获取stringio中的值
print(str1.getvalue())


#读取stringio对象中的数据
str2 = StringIO("hello\nyou are very good\n!!!")
print(str2.readline())
print(str2.readline())
print(str2.readline())
