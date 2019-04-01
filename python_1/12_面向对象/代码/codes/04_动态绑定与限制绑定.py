class Person():
	def sayHello(self):
		print("hello")

# 动态绑定: 声明类时,没有指定的属性, 在生成对象之后,动态添加
p1 = Person()
p1.name = "xiaoming"        # 动态添加属性
p1.money = 1000
p1.age = 20
print(p1.name)

p1.sayHello()


# 限制绑定: 只能使用特定的属性, 如果是其他的属性, 则报错
class Person():
	# 限制这个类,只能使用这两个属性
	Person.__slots__ = ("name","age")

# 只允许Person对象使用name,和age属性,使用其他的就会报错
p1 = Person()
p1.name = "zhangsan"
p1.age = 20
# p1.money = 1000    # 运行报错
