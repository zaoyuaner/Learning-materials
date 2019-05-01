# 顺序查找  遍历列表，挨个进行比较
list1 = [1,5,8,2,44,31,100]
key = 44
for index,item in enumerate(list1):
	if item == key:
		print("找到了","下标是:",index)
		break

# 二分查找（折半查找，基于一个有序列表.升序 ,降序）
list1 = [1,5,9,10,27,88,100]
left = 0                    # left 最开始指向第0个元素
right = len(list1)-1        # right 最开始指向最后一个元素
key = 100                   # 要找的数
while left <= right:
	middle = (left+right)//2
	# 我们要找的数,比中间这个数大,下标加1,往右移1
	if key > list1[middle]:
		left = middle +1

	# 要找的数比中间这个小,说明在左边,下标减1.往左移
	elif key < list1[middle]:
		right = middle -1
	else:
		print("找到了,下标是:",middle)
		break
else:
	print("这个数不存在该列表中")

	# 当key值不在列表中时,会出现left>right,会结束循环.


