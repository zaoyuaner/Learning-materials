#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author：zhangjiao
print()
'''
循环的嵌套:
for x in list1:
    for j in list2:
        循环体
执行过程: 先进入外循环,外循环走一遍,进入内循环,将内循环执行完毕之后
再执行外循环的下一轮,如此类推.
'''
list1 = [1,2,3,4]
list2 = ["hello","good","nice","great"]
for x in list1:
    print(x)
    for j in list2:
        print(j)

# # print("hello",end=" ")
# print("good")
'''
九九乘法表
行  列
1   1
2    2
3   3
...
9   9

两个循环:
外循环控制行,内循环控制列
'''
# for x in range(1,10):  #x=1  x=2  x=3
#     for j in range(1,x+1):#j=1
#         print("%dx%d=%d"%(j,x,x*j),end="\t")
#     #换行
#     print()


