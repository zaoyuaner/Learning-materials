#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author：zhangjiao
print()
'''
多分支：
语法：
if 判断条件1:
    语句块1
elif 判断条件2:
    语句块2
elif 判断条件3：
    语句块3
...
else:
    语句块n

执行过程：进入if语句，先执行判断条件1，若条件成立，则执行语句块1，
其他语句不再执行，若条件不成立，则执行判断条件2，若条件成立则执行语句块2，
其他的语句不再执行，依次类推，若所有的判断条件都不成立，则执行else下面的语句
'''
'''
需求：从控制台输入一个分数，判断这个分数的等级：
0~60:不及格
60~75：及格 x>=60 and x<75   
75~85：良好
85~100：优秀
'''
score = float(input("请输入您的成绩："))
# if score<60 :
#     print("不及格")
# elif score>=60 and score<75:
#     print("及格")
# elif score<85:
#     print("良好")
# else:
#     print("有点优秀")

'''
需求：从控制台输入一个分数，判断这个分数的等级：
要求对分数进行合法判断，若分数小于0或者大于100，输出”分数非法“
0~60:不及格
60~75：及格 x>=60 and x<75   
75~85：良好
85~100：优秀
'''

'''
分支语句的嵌套
if 判断条件1:
    if 判断条件2:
        语句块2
    else:
        语句块3
执行过程：先执行判断条件1，若条件成立，则执行判断条件2，若条件2成立则
执行语句块2，若不成立则语句块3.
一般情况下建议不要超过三层。
'''

if score>100 or score<0:
    print("成绩非法")
else:
    if score < 60:
        print("不及格")
    elif score < 75:
        print("及格")
    elif score < 85:
        print("良好")
    else:
        print("有点优秀")

if score>=0 and score<=100:
    if score < 60:
        print("不及格")
    elif score < 75:
        print("及格")
    elif score < 85:
        print("良好")
    else:
        print("有点优秀")
else:
    print("成绩非法")