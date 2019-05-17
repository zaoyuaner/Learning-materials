#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author：zhangjiao

'''
3.实现用户输入用户名和密码，当用户名为 seven且密码为123时，
显示登陆成功，否则登陆失败，失败时允许重复输入三次
'''
# count = 0
# while count<3:
#     count += 1
#     name = input("请输入用户名")
#     password = input("请输入密码：")
#     if name == "seven" and password == "123":
#         print("登陆成功！！！")
#         break
#     else:
#         print("登陆失败,您还剩%d次机会"%(3-count))
#         continue


'''
4.猜数字
很多人在聚餐时都玩过猜数字游戏，由某人随机出一个指定范围内的数，
然后其他人一个一个猜，猜的过程中区间不断缩小，直到猜中为止。
这里的猜数字游戏就是用程序来代替那个出数字的人，程序算法设计为：
1.输入数字区间--->2.系统产生区间内的随机数--->
3.玩家输入自己猜的数字--->4.比较玩家猜的与答案的高低并提示--->
5.未猜中则回到3，猜中则提示猜次数
'''
# import random
#
#
# count = 0
# start = int(input("请输入区间最小数："))
# end = int(input("请输入区间最大数："))
# num = random.randrange(start,end+1)
# # print(str(num).center(50,"*"))
# while True:
#     count += 1
#     num2 = int(input("请输入您猜测数字："))
#     if num == num2:
#         print("恭喜你猜对了，共用了%d次！！"%count)
#         break
#     elif num>num2:
#         print("小了")
#     else:
#         print("大了")

'''
5.2019个人所得税计算器
'''
money = int(input("请输入您当月工资："))
she = int(input("请输入您社保公积金扣除金额："))
mon = money - she
jiao = 0
if mon<=5000:
    jiao = 0
    print("贫困阶级，不用交税。。。")
elif mon<= 8000:
    jiao = (mon-5000)*0.03
    print("交税金额%.2f"%jiao)
elif mon<= 17000:
    jiao = (8000-5000)*0.03 + (mon-8000)*0.1
    print("交税金额%.2f"%jiao)
elif mon<=30000:
    jiao =  (8000-5000)*0.03 + (17000-8000)*0.1 + (mon-17000)*0.2
    print("交税金额%.2f" % jiao)
elif mon<= 40000:
    jiao = (8000 - 5000) * 0.03 + (17000 - 8000) * 0.1 + (40000 - 17000) * 0.2 +(mon-40000)*0.3
    print("交税金额%.2f" % jiao)





