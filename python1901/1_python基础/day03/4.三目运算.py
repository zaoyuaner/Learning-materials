#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author：zhangjiao
print()
'''
伪三目运算
将if else语句强制性写在一行的一个简单的运算。
语法：
result1  if 判断条件 else  result2
'''
a = 20
b = 10
# if a>b:
#     print(a)
# else:
#     print(b)
# print(a if a>b else b)
print(a) if a>b else print(b)

print('\n'.join([' '.join(['%s*%s=%-2s'%(y,x,x*y)for y in range(1,x+1)]) for x in range(1,10)]))

print('\n'.join([''.join([('LoveLove'[(x - y) % 8] if ((x * 0.05) ** 2 + (y * 0.1) ** 2 - 1) ** 3 - (x * 0.05) ** 2 * (
            y * 0.1) ** 3 <= 0 else ' ') for x in range(-30, 30)]) for y in range(15, -15, -1)]))