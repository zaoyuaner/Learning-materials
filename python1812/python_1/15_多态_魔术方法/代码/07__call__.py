
# 将对象当做函数调用时触发  方式:  对象()
class Boy:
	def __call__(self, *args, **kwargs):
		"""
		如果要把对象当函数调用时,需要重写该方法
		:param args: 任意位置参数
		:param kwargs: 任意关键字参数
		:return: 自定义
		"""
		print("call我")
		print(args,kwargs)

boy = Boy()
boy(1,2,33,name = "tom")     # 如果想把对象当做函数调用时,需要重写__call__函数


