#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author：zhangjiao
'''
字典：字典也是一个集合，它是一个无序集合，存储数据以key-value来进行存储的。
在python称为这种存储方式为字典，java称map集合，js称对象
对key的限制：
1.key必须是唯一的【在字典中key是不能重复的】
2.key必须是不可变的
常见的不可变类型：number/str/None/bool/tuple
可变类型：list/set/dict
'''

'''
字典的定义：
字典名 = {key1:value1,key2:value2,...,keyn:valuen}
元素与元素使用","隔开，key与value之间使用":"连接。

访问元素：
字典名[key]
使用这种方式访问，当key不存在的时候，会报错

字典名.get(key)
使用这种访问方式，当key不存在的时候，返回None，并不会报错。

添加元素：
字典名[key] = value

删除元素：
字典名.pop(key)
注意：key必须给，key若不存在，则报错。

'''


'''
存储所有同学成绩：
'''
list1 = [89,93,78]
list2 = [["张三",89],["李四",89]]
dict1 = {"张三":89,"李四":90}
dict1["张三"] = 70
print(dict1)
# print(dict1.get("王二"))
#
# dict1["王二"] = 79
# print(dict1)
#
# dict1["李四"] = [88,89]
# print(dict1)
#
# # print(dict1.pop("李四"))
# # print(dict1)
#
# #遍历key
# for x in dict1:
#     print(x)
#
# for x in dict1.keys():
#
# #dict1.values() 获取所有的value值
# for j in dict1.values():
#     print(j)
#
# # 同时遍历key与value
# for k,v in dict1.items():
#     print(k,v)
# '''
# 字典与list区别与联系：
# 1.都是集合，都是可变类型的
# 2.字典是无序的，list是有序的
# 3.存放方式不同，字典是以key-value的形式存储的，list存储value
# 4.list比字典节约空间
# 5.当数据量增加大情况下，list查询速度会因为数据量的增大而明显
# 变慢【从前往后查询】，而对于字典，对于它来说变化不大，它查询的
# 时候使用key来进行查询的。
# '''
# '''
# 从控制台录入6个同学的信息，
# 姓名，成绩
# 统计平均分，
# 把不及格的同学的名字与成绩打印出来。
# '''
# scoredict = {}
# while True:
#     name = input("请输入录入的姓名：")
#     score = int(input("请输入该同学的成绩："))
#     scoredict[name] = score
#     jixu = input("是否继续录入？yes/no")
#     if jixu == "yes":
#         continue
#     else:
#         break
#
# allscore = 0
# for n,s in scoredict.items():
#     if s<60:
#         print("名字：%s ,成绩 %d"%(n,s))
#     allscore += s
# print("平均分：%.2f"%(allscore/len(scoredict)))
#
#
#
