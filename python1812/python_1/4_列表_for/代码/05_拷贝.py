# 变量的复制分为三种

# 对象间引用

#   不可变对象: 数字,字符串,元组   不存在深拷贝
# #   可变对象: 列表,字典,集合    深拷贝针对于可变对象
# list1 = ["a","b","v"]
# list2 = list1        # 实质上是两个变量指向堆内存的同一片空间
# print(id(list1))
# print(id(list2))
#
# list2[1] = "hello"
# print(list1)        # 一改全改

# 浅复制        # 复制容器 不能产生副本
list1 = ['a','v',[1,2]]
list2 = list1.copy()         # 浅复制

list1[1] = "hello"
print(list2)

list1[-1].append(3)
print(list1)
print(list2)            # 外侧的列表无法改动,二维列表相互关联


# # 深复制   import copy   复制可变元素 产生副本
import copy
list1 = ["a","b","v"]
list2 = copy.deepcopy(list1)
print(list2)
list2[2] = "hello"
print(list1)
print(list2)