import os

def getAll(path):
	# 获取当前路径下的所有文件和文件夹
	filelist = os.listdir(path)
	# 获取每个文件或文件夹
	for i in filelist:
		# 拼接得到子目录
		filePath = os.path.join(path,i)
			# 判断 如果这个路径是一个目录,那么就应该继续往下进行遍历
		if os.path.isdir(filePath):
			getAll(filePath)
		else:
			print("文件:",filePath)     # 如果不是目录,那么就是文件



path = r"/Users/sorrisoyi/Desktop/python培训"
getAll(path)