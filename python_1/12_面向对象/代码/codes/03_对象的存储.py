# 通过同一个类,实例化出来的两个对象,他们所存储的地址不是同一个

class Person():
	name = "xiaoming"


	def show(self):
		print("show")

p1 = Person()           # p1是一个变量,指向堆内存中Person对象中的内存地址
p2 = Person()

print( id(p1))
print( id(p2))
