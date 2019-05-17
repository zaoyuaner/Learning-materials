#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author：zhangjiao
print()
'''
字符串:使用单引号或是双引号括起来的任意字符,我们称他为字符串.
str()  函数功能,将其他类型的数据转为字符串
'''

# str1 = "hello"
# str2 = ["world"]
# print(str1,str2)
'''
字符串的拼接
1.使用","拼接,会在逗号的位置产生一个空格
2.使用"+"拼接,要求数据类型必须相同
3.使用%拼接,格式化输出
4.使用"".join(l) 来进行拼接  序列中的元素必须为字符串

字符串的重复输出
str1*n  将str1重复输出n次

获取字符串中字符
str1[index] 通过索引值[下标]进行获取.
索引值从0开始  索引值的取值范围[0,len(str1))
若索引值为负数,则从右往左取[倒数第几个]

截取字符串
str1[start:end:step]
参数一:start[从start开始取] 开始默认0,若此字段不给,则从下标为0开始截取
参数二:end [取到end结束] 默认值len(str1),若此字段不给则截取到字符串末尾
参数三:step 步长默认1 [可以省略]
取值范围[start,end)

判断包含指定字符
str1 in str2
功能:判断str1是否是str2的字串,若是返回True,否则返回False
'''
str4 = "how are you"
str5 = "ey"
print(str5 in str4)

# print("体重%05d"%(123))
# print("体重%-5d"%(123))

str3 = input("请输入一个整数") #1234
print(str3)
print(str3[:2])
print(str3[2:])
print(str3[::2])
print(str3[::-1])

# print(str3[0])
# print(str3[1])
# print(str3[2])
# print(str3[-1])


# print(str1+str2)
# print(str1,123)
# print("%s %s"%(str1,str2))
# print("*".join(["hello","good","nice"]))
# print("*"*50)