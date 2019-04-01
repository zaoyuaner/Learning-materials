list1 = ["lisi","zhangsan","hack"]

#for循环  挨个访问列表中的元素.
for name in list1:
    print(name)      # 每个元素删除会出bug

# 利用索引(下标)遍历
for i in range(len(list1)):    # 0^4   ==>0 1 2 3
	print(list1[i])
else:
	print("遍历完毕")

