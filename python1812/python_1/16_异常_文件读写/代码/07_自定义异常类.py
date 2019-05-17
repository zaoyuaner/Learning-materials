# 如果系统异常类型满足不了业务需求，那么可以自己定义异常类来处理。
#
# 自己定义的异常类必须继承BaseException或Exception
# 步骤：
# - 在自定义异常类的构造函数中，调用父类构造函数
# - 重写`__str__`方法输出异常信息
# - 编写异常处理方法处理异常

class CustomError(BaseException):  # 继承BaseException
	def __init__(self, msg = ""):   # 输出信息默认为""
		super().__init__()  # 调用父类初始化
		self.msg = msg

	# 重写__str__，输出异常信息
	def __str__(self):
		if self.msg == "":
			return "错误,未知的错误"
		else:
			return self.msg

	# 3.自定义异常处理方法
	def handle_exception(self):
		print('异常处理')

try:
	raise CustomError('')
except CustomError as e:
	print(e)
	e.handle_exception()