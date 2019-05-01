import os
def getAll(path):
	# 栈
	stack = []
	# 入栈
	stack.append(path)
	# 栈为空,结束遍历
	while len(stack) != 0:
		# 出栈
		dirPath = stack.pop()

		# 获取当前目录下的所有文件
		filelist = os.listdir(dirPath)

		# 遍历当前目录下的所有文件
		for fileName in filelist:
			# 拼接得到文件名,或目录名
			filePath = os.path.join(dirPath,fileName)
			# 判断是不是路径
			if os.path.isdir(filePath):
				stack.append(filePath)     # 后进先出
				print(stack)
			else:
				print("文件:",filePath)

path = r"/Users/sorrisoyi/Desktop/pythonStudy"
getAll(path)
