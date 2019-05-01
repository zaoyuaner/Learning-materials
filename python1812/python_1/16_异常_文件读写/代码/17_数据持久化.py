# 数据持久化
# 数据持久化就是将内存中的对象转换为存储模型,以及将存储模型转换为内存中的对象的统称.
# 对象可以是任何数据结构或对象模型,存储模型可以是关系模型、XML、二进制流等

# pickled
# pickled可以将所有python支持的原生类型：布尔值，整数，浮点数，复数，字符串，字节，None。
# 以及由任何原生类型组成的列表，元组，字典和集合；函数，类，类的实例保存到文件

import pickle
a = {
	"name":"龙舟",
	"age": 21
}

# 写文件dump  要用二进制写入  wb
with open("02.txt","wb")as fp:

	pickle.dump(a,fp)

# 读取load   以二进制打开
with open("02.txt","rb") as fp:
	data = pickle.load(fp)
	print(data)
