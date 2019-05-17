import collections
import os

def getAll(path):
	# 队列
	queue = collections.deque()
	# 入队
	queue.append(path)
	while len(queue) != 0:
		# 出队
		dirPath = queue.popleft()
		# 获取当前目录下的文件列表
		fileList = os.listdir(dirPath)
		for fileName in fileList:
			# 获取文件列表中,文件的路径
			filePath = os.path.join(dirPath,fileName)
			# 如果这个路径是文件夹,那么需要入队,继续遍历
			if os.path.isdir(filePath):

				queue.append(filePath)
			else:
				# 不是文件夹,就打印出文件名,结束
				print("文件名:",filePath)
		print("---------------")
		print(queue)

path = r"/Users/sorrisoyi/Desktop/python培训"
getAll(path)

