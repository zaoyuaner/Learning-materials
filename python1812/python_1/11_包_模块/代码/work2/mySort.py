# 顺序查询  找出所有相同元素的下标[1,1,2,2,3,3,4,4]
# def myFind(key,list1):
# 	for i in range(len(list1)):
# 		if list1[i] == key:
# 			print("找到了,", "下标是:", i)
# 		continue
def findDuplicate(mylist):
	newlist = []
	for i in range(len(mylist)):          # i从第0个取到最末尾
		for j in range(i+1,len(mylist)):     # 每次都是从i+1到最末尾
			if mylist[i]  == mylist[j]:
				newlist.append(i)
				newlist.append(j)
	# 这个newlist会有重复的元素,需要去重
	newlist2 = []
	for item in newlist:
		if item not in newlist2:
			newlist2.append(item)
	return newlist2



# 二分查找
def getkeys(key,*args):
	list1 = sorted(args)               # 可以调用函数排序
	left = 0
	right = len(list1)-1
	while left <= right:
		middle = ( left + right ) //2
		if list1[middle] < key:
			left = middle +1
		elif list1[middle] > key:
			right = middle -1
		else:
			return middle
	return -1

# 冒泡排序
def BubbleSort(list1):                    # 传引用
	for i in range(len(list1)-1):
		for j in range(len(list1)-1-i):
			if list1[j] < list1[j+1] :
				list1[j],list1[j+1] = list1[j+1],list1[j]
	print(list1)

# 选择排序
def selectSort(list):
	for out in range(len(list)-1):
		min_index = out
		for inner in range(out + 1, len(list)):
			if list[inner] < list[min_index]:
				# 找到比list2[out]更小数的下标
				min_index = inner  # 记录下标
		list[out], list[min_index] = list[min_index], list[out]
	print(list)


