#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author：zhangjiao
'''
list1 = [1,2,22,34,45,66,77,1,2,3,4]
需要:将列表中元素进行去重处理
'''
list1 = [1,2,22,3,3,1,1,45,66,2,1,2,3,4]
list2 = []
for x in list1:
    if x in list2:
        pass
    else:
        list2.append(x)
print(list2)