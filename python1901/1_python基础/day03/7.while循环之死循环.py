#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author：zhangjiao
print()
'''
需求：
押宝，要求输入的汉字必须大或者小，若输入其他字符，
要求重新直到输入正确为止。
'''

'''
break 
作用：跳出循环体，结束循环
continue
作用：跳出本次循环，继续下一次【没有跳出循环体】
pass
作用：保持语意的完整
'''

# while 1:
#     ya = input("押大还是押小？大/小")
#     if ya in ["大","小"]:
#         print("输入正确。。。")
#         # break
#         # continue
#         continue
#         print("恭喜你输入正确")
#     else:
#         pass



'''
使用控制台打印1~100中所有的偶数
'''

# n = 1
# while n<=100:
#     if n%2==0:
#         print(n)
#     n += 1

n = 0
while n<=100:
    n += 1
    if n%2 != 0:
        continue
    print(n)
