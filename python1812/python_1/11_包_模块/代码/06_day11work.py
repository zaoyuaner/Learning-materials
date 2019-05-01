# 1.显示指定路径下所有视频格式文件，mp4，avi，rmvb

import os

def getMovieFiles(path):
#   1.首先判断路径是否正确
	if os.path.exists(path):
#   2.拿到路径下的所有文件及文件夹
		filelist = os.listdir(path)
#   3.遍历filelist,拼接路径与文件或文件夹,深入查找
		for fileName in filelist:
			filePath = os.path.join(path,fileName)
#   4.判断filePath是不是文件
			if os.path.isfile(filePath):
#   5.判断是不是指定格式的文件
				if filePath.endswith("mp4") or filePath.endswith("avi")\
				or filePath.endswith("rmvb"):
					print("文件名:",fileName)
			else:
				print(fileName,"不是文件")

	else:
		print("错误路径!")

getMovieFiles(r"/Users/sorrisoyi/Documents/听/MV")

# 2.自定义模块
#      建立一个包
#      在包的下创建一个排序的模块
#   模块下的功能
#       1.使用冒泡排序对列表进行降序排序
#       2.使用选择排序对列表进行升序排序
#       3.使用二分法查找的方式查找列表的元素
#           找到返回脚标
#           找不到返回 - 1
#       4.使用顺序查询，获取列表中所有重复元素的脚标
#
# 在另外一个文件中导入上述包中的模块，完成模块中功能的调用
from work2.mySort import *
# 1.冒泡排序
list1 = [333,12,122,412,556,754,3,23,1,99]
BubbleSort(list1)
# 不想改变list1，只想拿到排序后的副本
# import copy
# list2 = list1,copy()             # 进行列表的浅拷贝，排序list2 ,不修改list1


# 2.选择排序
selectSort([23,4,1,22,34,19,25,15])

# 3.二分法查找
getkeys(13, 4, 5, 88, 13, 40, 3, 12, 55, 66, 0, 2)

# 4.顺序查询
# import work2.OrderQuery
# work2.OrderQuery.myFind(3,[i for i in range(1,10)])
list3 = [333,12,122,412,556,754,3,23,3,99]
result = findDuplicate(list3)
print(result)