#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author：zhangjiao
print()
'''
数字类型之间的转换
str,int --> float
float(num)

str，float --》 int
int(num)

注意：当我们将字符串转为int/float类型的时候，只要是合法的
字符串都可以转换。【正负号是可以识别的】

'''
'''
常用的数据函数
abs(num)  返回num的绝对值
max(num1,num2,num3,...) 返回num中最大的那个值
min(num1,num2,num3,...) 返回num中最小的那个值
pow(x,y) 返回x的y次方
round(x[,n]) 保留x的n位小数，若n不写则默认保留整数
四舍五入，在py3.x 若出现.5的时候，默认向偶数靠拢

'''

'''
内置函数：
input、print、abs、max、min
自己没有定义，也没有引入，可以直接调用的函数，
我们称之为内置函数。
'''

print(abs(10))
print(abs(-10))

print(max(10,20,30,50,12,34))
print(min(10,20,30,50,12,34))

print(pow(2,3))

print(round(12.345))
print(round(12.555,2))
print(round(13.565,2))
# num = float(input("请输入一个数字："))
# print(num)
# print(type(num))
#
# num2 = int(input("请输入第二个数字"))
# print(num2)
# print(type(num2))
#
# print(num+num2)


