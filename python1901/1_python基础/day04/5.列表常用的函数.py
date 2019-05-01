#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author：zhangjiao
print()
'''
插入元素:
list1.append(object)
功能:在列表的末尾追加元素.

list1.extend(iterable)
iterable:能放在for循环中in后面的对象就是可迭代对象.
功能:将可迭代对象中元素,取出打碎插入.

list1.insert(index,object)
功能:在指定的下标处插入元素,原本位置上的元素向后顺延[不会发生数据覆盖]
'''

# list1 = []
# list1.append("张三")
# print(list1)
# list1.append("李四")
# print(list1)
# list1.append(["王五",20])
# print(list1)

# list1.extend("hello")
# print(list1)
# list1.extend([1,2,3])
# print(list1)

# list1.extend((1,2,3))
# print(list1)
# list1.extend({11,22,33})
# print(list1)
#
# list1.extend({"hello":11,"good":22,"nice":33})
# print(list1)
# list1.insert(0,"张三")
# print(list1)
# list1.insert(0,"李四")
# print(list1)

'''
删除元素
list1.pop(index)
index默认为-1,默认删除最后一个元素
若指定index,则删除下标为index所在位置元素,若index则报错.
并且它还会将删除的元素返回.

list1.remove(元素)
功能:移除第一个匹配到的元素,若匹配不到则报错.

list1.clear()
功能:清除列表中所有的元素,列表还存在.

del list1
功能:直接删除列表.
'''
# print("*"*50)
# print(list1)
# print(list1.pop())
list1 = [1,2,3,4,5,6,7,8]
# print(list1.pop())
# print(list1)
# print(list1.pop(0))
# print(list1)
# print(list1.pop(3))
# print(list1)
# print(list1.pop(-1))
# print(list1)
# list1.remove(1)
# print(list1)
#
# list1.clear()
# print(list1)

# del list1
# print(list1)
'''
list1.count(object)
功能:统计某个元素在列表中出现的次数


len(list1)
功能:获取列表的长度

max(list1)
功能:返回list1最大的元素

min(list1)
功能:返回list1最小元素

list2.reverse()
功能:将list2中元素倒叙，在原列表中进行操作

list2.sort(reverse=False)
功能:对列表中的元素进行排序,默认为升序,若reverse=True则为降序
'''
print(list1.count(1))
#
list2 = [111,2,3,45,56,54,78]
# list3 = [11,22,333,45,56,54,78]
# print(max(list2))
# print(min(list2))
#
# print(list2)
list2.reverse()
print(list2)
# print(list2[::-1])
list2.sort(reverse=True)
print(list2)



