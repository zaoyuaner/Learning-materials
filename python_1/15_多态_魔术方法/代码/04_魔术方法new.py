# __init__ 和__new__
# __init__ : 初始化对象
# __new__ : 创建一个对象, 有返回值

class Dog:
	# new负责给对象分配内存 , 类方法(参数cls) , 先于init运行
	def __new__(cls, *args, **kwargs):   # new可实现特殊需求,限制实例化对象
		print("__new__")
		# 必须通过父类调用new, 否则会无限递归
		obj = object.__new__(cls)
		print(obj)
		return object.__new__(cls)       # 返回对象的地址


	# init负责初始化对象 , 对象方法(参数self) , 后于new运行
	def __init__(self,name,age):
		self.name = name
		self.age = age
		print("__init__")

dog = Dog("黑背",10)
print( id(dog))
# __new__ 触发时机: 实例化对象的时候给对象分配内存时自动调用,cls代表类名,返回对象的地址

# __init__ 触发时机: 初始化对象时自动调用, self代表当前对象
