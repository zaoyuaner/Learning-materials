#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author：zhangjiao
'''
1.输入一个年份，判断是否为闰年。

条件1：不能被100整除且能被4整除

条件2：被400整除【世纪年】
'''
# year = int(input("请输入一个年份"))
# if year%4==0 and year%100!=0 or year%400==0:
#     print(year,"为闰年")
# else:
#     print("%s不为闰年"%(year))

'''
2.输入一位三位数，判断是否为水仙花数153
153 = 1^3+5^3+3^3
'''
# 345
# num = int(input("请输入一个三位数"))
# ge = num%10
# shi = num//10%10
# bai = num//100
# if num == ge**3 + shi**3 + bai**3:
#     print("%d为水仙花数"%num)
# else:
#     print("%d不是水仙花数"%num)

'''
3.输入一个五位数，判断是否为回文数 12321
'''
# num = int(input("请输入一个五位数："))
# ge = num%10
# wan = num//10000
# shi = num//10%10
# qian = num//1000%10
#
# if ge==wan and shi==qian:
#     print("%d为回文数"%num)
# else:
#     print("%d不是回文数"%num)

'''
4.摇色子，
提示:押大还押小  ： 大  或者 小
开始摇色子，
【1~6】取值【1， 2， 3】 小
 取值【4， 5， 6】大
若押中，则打印“庄家喝酒。。。。“
若没押中，则打印”先干为敬。。。“
'''
import random

print("开始游戏")
jiang = random.randrange(1,7)
print(jiang)
ya = input("押大还是押小？大/小")
if ya=="大" and jiang>3 or ya=="小" and jiang<4:
    print("庄家喝酒。。。。")
else:
    print("先干为敬。。。")







