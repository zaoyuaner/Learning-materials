#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author：zhangjiao
'''
1、字符串的替换
str1.replace(old,new,count)
old:旧字符串
new：新字符串
count:替换的次数
功能：使用新的字符串将旧的字符串进行替换，并返回替换后的字符串

2、字符串的隐射替换
table = str1.maketrans（old，new）
old -- new 字符一一对应
str2.translate(table)

str2.startswith(str1,start,end)
判断str2是否以str1开头，若指定start和end，则判断指定范围内的
若不指定，则默认整个字符串。

str2.endswith(str1,start,end)
判断str2是否以str1结尾，若指定start和end，则判断指定范围内的
若不指定，则默认整个字符串。

字符串的编码：
str1.encode("utf-8")  对字符串进行编码
str1.decode("utf-8") 对字符串进行解码

'''

# str1 = "you are a good man, you are a great man"
# print(str1.replace("man","dog",3))
#
# str2 = "you are a good man！"
# table = str1.maketrans("you","123")
# print(str2.translate(table))

# print(str1.startswith("you",20,40))
# print(str1.endswith("man",0,10))
#
# str3 = "中国"
# str4 = str3.encode("utf-8")
# print(str4)
# print(str4.decode("utf-8"))
'''
str1.isalpha()
功能：判断字符串中所有的字符是否都为字母，若是则返回True
否则返回False【不考虑中文】

str1.isalnum()
功能：判断字符串中所有的字符是否都为字母或者数字，若是则返回True
否则返回False【不考虑中文】

str1.isupper()
判断str1中字符是否全部为大写字母，若是返回True，否则返回False

str1.islower()
判断str1中字符是否全部为小写字母，若是返回True，否则返回False

str1.istitle()
判断str1中字符是否全部为标题化的字符串，若是返回True，否则返回False

str1.isspace()
判断str1中字符是否全部为空白符，若是返回True，否则返回False
'''
str5 = "Hello"
str6 = "hello1"
str7 = "hello$中国"
# print(str5.isalpha())
# print(str6.isalpha())
# print(str7.isalpha())
# print(str5.isalnum())
# print(str6.isalnum())
# print(str7.isalnum())

str9 = "1HJUI11中国"
# print(str5.isupper())
# print(str9.isupper())
# print(str5.islower())
# print(str9.islower())
#
# print(str5.istitle())
# print(str9.istitle())

print("".isspace())
print("\n".isspace())
print("\t".isspace())
print("\r".isspace())
print(" ".isspace())