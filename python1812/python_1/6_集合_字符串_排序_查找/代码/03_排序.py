# 冒泡排序   # 两两相比,大者后移,较大数往后
	# list1 = [4,9,20,16,7,8,40,23]     # 先进行4,9的比较,不交换,进行9,20交换,不交换,在进行20和16的比较,交换
	# list1 = [4,9,16,20,7,8,40,23]     # 20和7的比较,交换
	# list1 = [4,9,16,7,20,8,40,23]     # 20和8的比较,交换
	# list1 = [4,9,16,7,8,20,40,23]     # 20和40的比较,不交换,40和23的比较,交换
	# list1 = [4,9,16,7,8,20,23,40]     # 进行一轮比较后的结果

list1 = [4,9,20,16,7,8,40,23]    # 内循环只是做了一轮替换,套一个外循环进行多次
	# 因为这个inner会取到列表最大值,再加一就会越界,所以在外层循环-1
for out in range(len(list1)-1):   # 8个数最大下标为7,控制轮数
	for inner in range(len(list1)-out-1):  # -out用于减少次数,可以不减,inner+1会越界,所以-1
	# 因为每一轮排序都会确定一个最大的数,放到最后面,所以下一次循环就可以少一次比较
		if list1[inner] > list1[inner+1]:   # 改成< 就是降序
			list1[inner],list1[inner+1] = list1[inner+1],list1[inner]
print(list1)       # 总是相邻两个数相比

# 选择排序   先寻找最小数的下标,先记录下来,最后只进行一次交换,较小数往前
list2 = [4,9,16,7,8,20,3,23,40]
	# 先认为第0个元素就是最小,遍历列表,去寻找比这个4更小的数
for out in range(len(list2)):
	# 使用min变量保存最小数
	min_index = out
	for inner in range(out+1,len(list2)):
		if list2[inner] < list2[min_index]:   # 改成> 就是降序
			# 找到比list2[out]更小数的下标
			min_index = inner     # 记录下标
	# 进行一次交换
	list2[out],list2[min_index] = list2[min_index],list2[out]
print(list2)


