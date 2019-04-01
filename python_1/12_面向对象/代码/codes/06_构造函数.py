# 如果使用类属性,来定义对象的名字,那么实例化出的对象,名字都会相同

# 构造方法
class Person():
	# 作用是: 进行数据的初始化
	# 调用时机: 当对象实例化时,自动被调用
	def __init__(self):
		print("构造方法被调用了")

# 如果自己不写__init__,那么系统会自动为你调用,然后在创建对象
# 如果自己写了__init__,那么实例化对象时,会调用自己写的构造方法

# 带参的构造函数
class Person2():
	# 类属性
	# name = ""
	# age = 0
	# def __init__(self):
	# 	# 在对象实例化时,为name和age赋值
	# 	name = "xiaoming"       # 这个name 只是__init__ 函数中的局部变量,
	# 							# 调用后会被释放,所以这个对象属性赋初值无效
	# 	age = 20
	def __init__(self,name,age):
		self.name = name        # 对象属性
		self.age = age

	# 不定长参数构造函数
	# def __init__(self,*args):

# p = Person()
# print( p.name)         # 空
# 如果构造函数有参数,实例化类时,必须带上一样的参数
p = Person2("小明",20)
print( p.name)
print( p.age)

p2 = Person2("tony",40)
print( p2.name)
print( p2.age)

# 总结:  构造函数在对象创建时,就会自动调用,它的作用就是为每个对象的属性赋值.