class Dog:
	def __init__(self,name,age):
		self.name = name
		self.__age = age
	def __getattr__(self, item):
		"""
		当获取对象私有或不存在的属性时自动调用
		:param item: 访问的属性名
		:return: 自定义
		"""
		if item == "age":
			print("私有属性无法访问")
		else:
			return self.__dict__[item]

dog = Dog("钉钉",5)
print(dog.__dict__)
print(dog.name)
print(dog.age)           # 私有属性无法访问
