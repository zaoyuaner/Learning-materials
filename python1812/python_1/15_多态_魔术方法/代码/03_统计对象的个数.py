# 示例 统计对象的个数

class Dog:
	num = 0
	def __init__(self):
		# Dog.num += 1
		self.__class__.num +=1      # 通用写法

	def __del__(self):
		# Dog.num -= 1
		self.__class__.num -= 1

d1 = Dog()
d2 = Dog()
print(Dog.num)
del d1
print(Dog.num)
d3 = Dog()
d1 = Dog()
print(Dog.num)

