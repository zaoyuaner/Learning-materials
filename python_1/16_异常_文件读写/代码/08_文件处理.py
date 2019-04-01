# 文件处理  数据持久化
# 1.文件读取: 打开文件 --> 读取内容(read,readline,readlines) --> 关闭文件
# fp 是一个可迭代对象
fp = open("1.txt", mode= "r")      # 打开文件,如果编码格式错误,加入encoding="UTF-8"
print(fp)

# data = fp.read()           # 读取文件 read不带参数全部读取
# data1 = fp.read(3)         # 带参数读取指定字符个数
# print(data)
# print(data1)             # 鲲之大

# data = fp.readline()         # 读取行, 一行一行的读取, 会接着上一行
# data = fp.readline()         # 带参数读取指定字符个数
# data = fp.readline()
# print(data)
# 用while循环
# data = "1"
# while data:
# 	data = fp.readline()        # 会把每行后面的换行符读进来
# 	print(data.strip())         # strip()去掉换行符

# readlines                   # 读取多行   返回一个列表
data2 = fp.readlines()
print(data2)

fp.close()        # 关闭文件