#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author：zhangjiao

print()
'''
分支语句：
语法：
单分支结构
if 判断条件:
    语句块
执行过程：先执行判断条件，若判断条件成立，则执行if下面的语句块，
若判断条件不成立，则不执行
双分支：
if 判断条件:
    语句块1
else:
    语句块2

执行过程：先执行判断条件，若判断条件成立，则执行if下面的语句块，
若判断条件不成立，则执行else下面的语句块
'''


'''
需求：网吧规定，未成年人禁止进入。
'''
# age = int(input("请输入您的年龄"))
# if age<18:
#     print("未成年禁止进入")
# else:
#     print("欢迎光临！！")

'''
需求：妈妈说，英语、数学、语文有一门挂科就没饭吃。。。
'''
english = float(input("请输入您的英语成绩"))
math_ = float(input("请输入您的数学成绩"))
chinese = float(input("请输入您的语文成绩"))
# if english<60 or math_<60 or chinese<60:
#     print("回来跪地板。。。")
# else:
#     print("今晚吃鸡。。。")

'''
需求：妈妈说，英语、数学、语文平均分不及格,或者两门及两门以上挂科就没饭吃.
'''
evg = (english+math_+chinese)/3
print(evg)
if evg<60 or (english<60 and math_<60) or (english<60 and chinese<60) or (math_<60 and chinese<60):
    print("回来跪地板。。。")
else:
    print("今晚吃鸡。。。")


