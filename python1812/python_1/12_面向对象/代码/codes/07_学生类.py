class Student():
	def __init__(self,name,age,hobby):
		self.name = name
		self.age = age
		self.hobby = hobby

xiaoming = Student("小明",20,"唱歌")         # 对象一被创建,就自动调用init函数
xiaoli = Student("小丽",20,"跳舞")

print(xiaoming.name)
print(xiaoming.age)
print(xiaoming.hobby)