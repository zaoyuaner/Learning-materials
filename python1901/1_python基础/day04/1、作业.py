#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author：zhangjiao
'''
1.计算1~100以内所有能被3或者17整除的数的和
'''
# res = 0
# for i in range(1,101):
#     if i%3==0 or i%17==0:
#         res += i
# print(res)

'''
2.计算100~999的水仙花数的个数，并且打印水仙花数
'''
# count = 0
# for i in range(100,1000):
#     i = str(i)  #123 -->"123"
#     if int(i[0])**3 + int(i[1])**3 + int(i[2])**3 == int(i):
#         print(i)
#         count += 1
# print(count)

'''
3.计算10000~99999回文数的个数，并且打印回文数的个数
'''
# count = 0
# for x in range(10000,100000):
#     x = str(x)
#     if x[0] == x[4] and x[1] == x[3]:
#         print(x)
#         count += 1
# print(count)

'''
4.计算200~500以内能被7整除但不是偶数的数的个数。
'''
# count = 0
# for x in range(200,501):
#     if x%7==0 and x%2!=0:
#         count += 1
#
# print(count)
'''
5.使用for循环打印九九乘法表，倒过来
'''
# for i in range(1,10):
#     for j in range(1,i+1):
#         print("%dx%d=%d"%(j,i,j*i),end="\t")
#     print()

'''
9x9=81	8x9=72	7x9=63	6x9=54	5x9=45	4x9=36	3x9=27	2x9=18	1x9=9	
		8x8=64	7x8=56	6x8=48	5x8=40	4x8=32	3x8=24	2x8=16	1x8=8	
				7x7=49	6x7=42	5x7=35	4x7=28	3x7=21	2x7=14	1x7=7	
						6x6=36	5x6=30	4x6=24	3x6=18	2x6=12	1x6=6	
								5x5=25	4x5=20	3x5=15	2x5=10	1x5=5	
										4x4=16	3x4=12	2x4=8	1x4=4	
												3x3=9	2x3=6	1x3=3	
														2x2=4	1x2=2	
																1x1=1
		i 控制行   总共9行  第一行i=9   9列    0个空格 9-i
		j 控制列           第二行 i=8  8列     1个
		k 控制空格		  第三行	i=7  7列    2个										


'''


# for i in range(9,0,-1):  #i=9  i=8
#     for k in range(9-i): #不会打印[0,0)  #k=0 [0,1)
#         print("\t",end="\t")
#     for j in range(i,0,-1): #j=9-->1 #j=8-->1
#         print("%dx%d=%d"%(j,i,i*j),end="\t")
#     print()


'''

6.押宝游戏：
开始游戏 -> 投入赌金【一次性投入】 ->
循环  ：押宝【5块钱一次】 -> 开奖  --》中奖/未中奖 --》用户输入是否继续 【当余额不足则自动退出游戏】
'''
import random


# print("开始游戏")
# money = int(input("请投入您的赌金:"))
#
# while True:
#     if money >= 5:
#         jiang = random.randrange(1, 7)
#         ya = input("押大还是押小?大/小")
#         money -= 5
#         if jiang > 3 and ya == "大" or jiang < 4 and ya == "小":
#             print("恭喜你中了一个大白!!!")
#         else:
#             print("很抱歉没中奖,继续努力!")
#         print("您当前余额为%d"%money)
#         jixu = input("是否继续游戏?yes/no")
#         if jixu == "yes":
#             continue
#         else:
#             print("退出游戏")
#             break
#     else:
#         print("余额不足,退出游戏")
#         break

'''
7.百钱买百鸡，现有100文钱，公鸡5文钱一只，母鸡3文钱一只，小鸡一文钱3只.要求：公鸡，母鸡，小鸡都要有，
把100文钱买100只鸡，买的鸡是整数。多少只公鸡，多少只母鸡多少只小鸡？
公鸡[1,20)  i
母鸡[1,33)  j
小鸡[3,98)  k
'''
# for i in range(1,20):
#     for j in range(1,33):
#         for k in range(3,98,3):
#             if i+j+k == 100 and 5*i+3*j+k/3==100:
#                 print("公鸡%d,母鸡%d,小鸡%d"%(i,j,k))



'''
要求从控制台输入一个电话号码,判断电话号码是否合法:
11位,并且全部为数字.
'''
# phone = input("请输入一个电话号码")
# if len(phone) != 11:
#     print("电话号码长度非法")
# else:
#     for x in phone:
#         if x>='0' and x<='9':
#             pass
#         else:
#             print("电话号码不合法")
#             break
#     else:
#         print("此电话号码合法...")

'''
写代码，有如下变量，请按照要求实现每个功能
name = " alleX "
a.移除name变量对应的值两边的空格,并输出
b.判断name变量对应的值是否以 "al"开头，并输出结果
c.判断name变量对应的值是否以 "X"结尾，并输出结果
d.将name变量对应的值中的 " l" 替换为 " p"，并输出结果
e.将name变量对应的值根据 " l" 分割，并输出结果。
f.请问，上一题 e分割之后得到值是什么类型？
g.将name变量对应的值变大写，并输出结果
h.将name变量对应的值变小写，并输出结果
i.请输出name变量对应的值的第2个字符？
j.请输出name变量对应的值的前3个字符？
k.请输出name变量对应的值的后2个字符？
l.请输出name变量对应的值中 "e" 所在索引位置？
使用代码表示
'''
# name = " alleX "
# # name = name.strip()
# print(name)
# print(name[:2]=="al")
# print(name[-1]=="X")
# name2 = ""
# for x in name:
#     if x=="l":
#         name2 += "p"
#     else:
#         name2 += x
# print(name2)
# print(name.split("l"))
# print("列表")
# print(name.upper())
# print(name.lower())
# print(name[1])
# print(name[:3])
# print(name[-2:])
# print(name.find("e"))

for i in range(1,10):
    for j in range(1,i+1):
        print("%dx%d=%d"%(j,i,j*i),end="\t")
    print()