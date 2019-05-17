#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author：zhangjiao
print()
'''
%s  表示字符串
%d 表示int类型
%02d 表示占用两位，高位不够补0
0:占位符  2：代表长度
%f  表示浮点型
%.2f 表示浮点数保留两位小数
'''

print("我是%s,今年%d,语文考了%.2f分"%("lili",20.3,89.7))
print("我是%s,今年%d,语文考了%.2f分"%("lili",20,89.7))
print("当前时间%d:%02d:%d"%(10,4,12))