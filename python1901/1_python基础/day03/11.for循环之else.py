#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author：zhangjiao
print()
'''
for 变量  in 序列:
    循环体
else:
    语句块

执行过程:先执行for循环,for循环正常执行结束再执行else,
若为非正常执行结束,则不执行else下面的语句块.
break,continue,pass三个关键字在for循环中同样适用.
break,continue是在循环中使用[while,for]
'''

# for x in range(10):
#     print(x)
#     if x>5:
#         break
# else:
#     print("正常循环结束")

for i in "hello":
    print(i)