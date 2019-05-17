#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author：zhangjiao
'''
生成1，2，3，...,100序列，一行代码
生成1，4，9，...,10000,一行代码实现
列表生成式：
本质：将for循环强制性的写在一行，把结果写在最前面，然后使用[]括起来。
语法：
[结果 for x in range() 语句]
生成1，4，9，...,10000, 去除7的倍数 一行代码实现
'''
# print(list(range(1,101)))
# list1 = []
# for x in range(1,101):
#     list1.append(x*x)
# print(list1)

# print([x*x for x in range(1,101)])
# #
# # print([x*x for x in range(1,101) if x*x%7 !=0])
# # print([x*x for x in range(1,101) if x*x%7])
# #
# # print('\n'.join([' '.join(['%s*%s=%-2s'%(y,x,x*y)for y in range(1,x+1)]) for x in range(1,10)]))

print([x*x for x in range(1,101) if x*x%7 != 0])