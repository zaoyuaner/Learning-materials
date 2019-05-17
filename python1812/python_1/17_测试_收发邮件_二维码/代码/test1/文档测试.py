import doctest

def mul(a,b):
	"""
	乘法
	:param a:
	:param b:
	:return:  a乘以b的结果

	>>> mul(3,4)
	12
	"""                 # 上面的两行后面不能接任何注释. 且放在"""内

	return a*b

if __name__ == "__main__":

	doctest.testmod()                # 测试失败 .测试成功不会返回值
