#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author：zhangjiao
print()
'''
列表的组合
list1 + list2
功能:给返回一个新的列表,两个列表中元素的重新组合.
'''
list1 = [1,2,34]
list2 = [4,5,6]
print(list1+list2)

'''
列表的重复
list1*n
功能:将list1中的元素重复输出n次,并且返回一个新的列表.
'''
print(list1*3)

'''
判断某个元素是否存在列表中
元素 in 列表
若存在返回True,否则返回False
'''
print(3 in list1)

'''
列表的截取
list1[start:end:step]
参数一:从start开始截取,默认0
参数二:截取到end结束end默认len(list1),end取不到
参数三:步长 默认1
截取的范围[start,end)
'''
print(list1[::-1])

'''
二维列表:
list1 = [列表1,列表2,...,列表n]
二维列表元素的访问:
list1[index1][index2]
index1:代表第几个列表
index2:列表中第几个元素
'''
list3 = [[["张三",20,80],"李四"],["王二","狗蛋"],["张飞","刘备","关羽"]]

print(list3[0][0][0])
print(list3[1][1])
print(list3[-1][1])


list2=[1,2,3,4]
print(list2[::-2])
print(list2[1::2])