# 元组:只读的列表
tuple1 = ()   # 空元组
tuple2 = (1,2,3,4,5)
print(tuple1)
print(tuple2)

tuple3 = (2,"hello",True)

tuple4 = (5+4)     # 括号用于提升优先级,不会当做元组,会当成数字处理
tuple5 = (5)
print(tuple4)
print(type(tuple5))

tuple5 = (5,)
print(type(tuple5))     # 如果元组只有一个元素,需要多加一个逗号

tuple7 = ("a","b","c","d")     # 元组元素也能通过索引获取
print(tuple7[0])
print(tuple7[-1])

tuple8 = (1,2,3,[5,6,7])
# tuple8[-1] ="hello"   #  不允许修改
tuple8[-1][0] = 20      #  可以修改元组中的列表中的元素,整体不允许修改
print(tuple8)

# 元组可以被整体删除
del tuple8

# +合并元组,返回新元组
tuple1 = (1,2,3)
tuple2 = (4,5,6)
tuple3 = tuple1 + tuple2
print(tuple3*3)         # 重复三次

# in  not in
print(1 in tuple1)

# 和列表一样支持切片
print(tuple1[1:])
print(tuple1[-1:])    # (3,)

# 求长度
print(len(tuple1))
print(max(tuple1))

# 元组和列表互转
list1 = ["a","b","c"]
print(tuple(list1))     # 列表转元组

print(list(("a","b","c")))    # 元组转列表

# 遍历   三种方式:for,下标,枚举
for item in tuple2:
	print(item)

for i in range(len(tuple2)):
	print(tuple2[i])

for index,item in enumerate(tuple2):
	print(index,item)

# 二维元组
tuple3 = (("a","b","c"),(1,2,3),("A","B"))
for item in tuple3:     # ("a","b","c")
	for item2 in item:
		print(item2)

# 元组的解包
a = (1,2,2,3)
c,*_,d = a      # 1=c 3=d   *_ 忽略中间的,取两边的
print(c,d)