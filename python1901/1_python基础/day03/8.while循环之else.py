#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author：zhangjiao
print()
'''
while 判断条件:
    循环体
else:
    语句块

执行过程:从判断条件开始执行,若条件成立则执行循环体,循环体执行结束,继续执行
判断条件,循环往复,正常循环结束的时候将执行else下面的语句块,若是非正常结束,
则不执行else下面的语句块.
'''
n = 1
while n<=100:
    print(n)
    n += 1
    if n>50:
        continue
else:
    print("正常执行结束")

# while 1:print("hello")
'''
while 条件: 语句
当while循环只有一条语句的时候,我们可以将其写在一行
'''
while 3>2:print("zhengque")