# 二分法查找
list1 = [1,5,9,10,27,88,100,223,12]
list1.sort()                 # 使用二分法必须是升序或者降序的列表!!
print(list1)
# 二分法查找10

left = 0
right = len(list1)-1   # 8  长度为9
key = 10
while left <= right:
	middle = (left+right)//2
	if key > list1[middle]:
		left = middle +1
	elif key < list1[middle]:
		right = middle -1
	else:
		print("找到了,下标为:",middle)
		break
else:
	print("不在此列表中")

# 冒泡排序
list2 = [1000,2,66,8,5,34,23,900,13,90,2]
for i in range(len(list2)-1):
	for j in range(len(list2)-i-1):
		if list2[j] < list2[j+1]:     # 相邻两位相比
			list2[j],list2[j+1] = list2[j+1],list2[j]
print(list2)

# 选择排序
list2 = [1000,2,66,8,5,34,23,900,13,90,2]
for i in range(len(list2)):
	min_index = i
	for j in range(i+1,len(list2)):
		if list2[j] < list2[min_index]:
			min_index = j
	list2[i],list2[min_index] = list2[min_index],list2[i]
print(list2)
#
# for i in range(len(list2)):
# 	min_index = i
# 	for j in range(i+1,len(list2)):
# 		if list2[j] < list2[min_index]:
# 			min_index = j
# 	list2[i],list2[min_index] = list2[min_index],list2[i]
# print(list2)

