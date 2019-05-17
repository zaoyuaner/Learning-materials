# 遍历目录  path
import os               # os环境下使用

path = r"/Users/sorrisoyi/Desktop/python培训"     # r忽略转义
# os.listdir  显示当前路径下,所有的文件夹或文件
filelist = os.listdir(path)
print(filelist)

# 将path和day进行拼接,得到一个目录
filePath = os.path.join(path,"day1.11.18")
print(filePath)