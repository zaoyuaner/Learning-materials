"""
题目要求：
设计合理的类，完成以下功能：
1.把住宿记录读入，每条记录生成一个对象，将对象存到列表中
2.输入姓名，查询出相关记录
3.要求：如果性别是m，显示男，f显示女，字段值是-，显示无
"""
class Function(object):

	@classmethod
	def reader(cls,path):
		cls.mylist = []
		with open(path,"r") as fp:
			new_data = 1
			while new_data:
				data = fp.readline()
				new_data = data.replace("M","男").replace("F","女").replace("-","无")
				cls.mylist.append(new_data.strip())
			return cls.mylist

	@classmethod
	def finder(cls,name):
		import re
		list2 = []
		for j in cls.mylist:
			if re.match(name, j):
				list2.append(j)
		if list2 ==[]:
			return "查无此人"
		return list2

path = "kaifang.txt"

print(Function.reader(path))
print(Function.finder("王"))

class Message:
	pass


