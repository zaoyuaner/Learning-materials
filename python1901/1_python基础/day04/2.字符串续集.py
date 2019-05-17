#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author：zhangjiao
str1 = "开始游戏"
'''
# str1.center(width,fillchar)
# 功能:返回一个指定宽度文本居中的字符串,以fillchar来进行填充
# str1.ljust(width,fillchar)
# 功能:返回一个指定宽度文本居左的字符串,以fillchar来进行填充
# str1.rjust(width,fillchar)
# 功能:返回一个指定宽度文本居右的字符串,以fillchar来进行填充
# str1.zfill(width)
# 功能:返回一个长度为width字符串，原字符串右对齐，前面补0
'''
# print(str1.center(50,"%"))
# print(str1.ljust(50,"*"))
# print(str1.rjust(50,"*"))
print(str1.zfill(50))


'''
在定义字符串的时候,若字符串过长,我们可以使用三引号将其括起来
输出会保留字符串默认的格式
'''

str2 = '''
　　When I was dreaming about you baby
　　You were dreaming of me
　　Call me crazy
　　Call me blind
　　To still be suffering is stupid after all of this time
　　Did I lose my love to someone better
　　And does she love you like I do
　　I do, you know I really really do
'''

'''
str1.count(sonstr,start,end)
统计子串sonstr在str1中出现的次数,若指定范围,则统计指定范围内的,
若不指定,则统计整个字符串.
'''
# print(str2.count("I",0,20))
'''
str1.find(sub,start,end)
功能:在str1中从左往右查找sub子串,若子串存在,则返回子串第一个字母第一次出现的
所在的下标值.若找不到则返回-1

str1.rfind(sub,start,end)
功能:在str1中从右往左查找sub子串,若子串存在,则返回子串第一个字母第一次出现的
所在的下标值.若找不到则返回-1

str1.index(sub,start,end)
功能:在str1中从左往右查找sub子串,若子串存在,则返回子串第一个字母第一次出现的
所在的下标值.若找不到则报错

str1.rindex(sub,start,end)
功能:在str1中从右往左查找sub子串,若子串存在,则返回子串第一个字母第一次出现的
所在的下标值.若找不到则报错
'''
# print(str2.find("Call"))
# print(str2.rfind("Call"))
# print(str2.index("Call"))
# print(str2.rindex("Call"))
# print(str2.rindex("Cl"))

str3 = "   you are very good   "

phonenum = "***1234***343****"
'''
str1.lstrip(sub)
功能:去掉左边的指定的字符,若不指定,则默认去掉空白符[\n,\r,\t," "]

str1.rstrip(sub)
功能:去掉右边的指定的字符,若不指定,则默认去掉空白符[\n,\r,\t," "]

str1.strip(sub)
功能:去掉两边的指定的字符,若不指定,则默认去掉空白符[\n,\r,\t," "]
'''
# print(phonenum.lstrip("*"))
# print(phonenum.rstrip("*"))
# print(phonenum.strip("*"))
'''
str1.split(sub,maxsplit)
功能:以指定的字符串对str1进行切片,若不指定字符串,则默认以空白符进行切.
我们还可以指定最大切割次数,若不指定则默认全部切片.

str2.splitlines(keepends=False)
功能:按行切片,keepends=True 保留换行符,False默认 不保留
'''
print(str2.split(maxsplit=3))
print(str2.splitlines())
