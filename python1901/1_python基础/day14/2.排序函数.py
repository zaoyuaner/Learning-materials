#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author：zhangjiao
'''
sorted(iterable,key,reverse)
参数一：要排序的序列
参数二：以key来进行排序
参数三：升序reverse=False还是降序True
功能:将序列中的元素依次作用于key后面的函数，把作用后的结果按照指定排序方式进行排序。
'''
list1 = [1,2,34,434,232,34]
# list1.sort()
# print(list1)

print(sorted(list1))

list2 = [1,"2","3",44,"33","45",23]
'''
以字面量的形式排序
'''
print(sorted(map(int,list2)))
print(sorted(list2,key=int))

'''
以字符串长度的降序来进行排序
'''
list3 = ["111","33343","4t665gfhy","dfrfty"]

print(sorted(list3,reverse=True,key=len))

data= [["lili",28,"美食"],["tom", 25, "无"],["hanmeimei", 26, "金钱"]]
'''
按照年龄的升序来进行排序
'''

print(sorted(data,key=lambda x:x[1]))
