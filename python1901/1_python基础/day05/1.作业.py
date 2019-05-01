#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author：zhangjiao
'''
1.打印星星号
从控制台输入1
*
输入3
 *
***
 *
输入5
  *
 ***
*****
 ***
  *
依次类推
'''
# while True:
#     n = int(input("请输入一个奇数："))
#     if n%2 ==0:
#         print("这个数为偶数，输入非法，请重新输入。。。。")
#     else:
#         break
#
#
# for x in range(1,n+1,2):
#     print(("*"*x).center(n))
#
# for j in range(n-2,0,-2):
#     print(("*"*j).center(n))

'''
2.写一个双色球彩票系统，系统可以随机产生一组随机数据，一组彩票数据有六位数，
这六位数的的取值范围是0和1。[001001]一张彩票是两块钱，用户可以充值金额，
并且可以决定自己购买彩票的张数,若余额不足,则提示充值,若用户拒绝充值,则退出游戏
若余额充足,用户输入猜测的数据[要求输入的数据必须合法]，若是猜对，
则打印”恭喜你中大奖了“ 奖励的金额=投入金额*100，若没猜中则打印”继续加油！“。
用户可以选择继续买票或者是退出。买票和退出的时候要求打印剩余金额。
'''
import random
print("开始游戏".center(50,"*"))
money = 0
while True:
    money += int(input("请充值："))
    count = int(input("请输入购买彩票的张数："))
    if money>= count*2:
        money -= count*2
        print("余额充足")
        jiang = ""
        for x in range(6):
            jiang += random.choice(["0","1"])
        print("jiang=",jiang)
        yalist = []
        for _ in range(count):
            while True:
                ya = input("请输入您购买的号码：6位 0/1")
                if len(ya) == 6:
                    for i in ya:
                        if i in ["0","1"]:
                            pass
                        else:
                            print("输入数字非法。。")
                            break
                    else:
                        print("输入合法。。。")
                        break
                else:
                    print("输入长度非法")
                    continue
            yalist.append(ya)


        if jiang in yalist:
            print("恭喜你中大奖啦！！！")
            money += count*2*100
        else:
            print("很遗憾没中奖，继续努力！！！")

        print("您目前的余额为%d"%money)
        jixu = input("是否继续游戏？yes/no")
        if jixu == "yes":
            continue
        else:
            print("退出游戏。。。")
            break
    else:
        print("余额不足")
        cong = input("是否需要充值？yes/no")
        if cong == "yes":
            continue
        else:
            print("余额不足退出游戏")
            break
