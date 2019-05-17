# ***错误*** 指的是代码有语法问题，无法解释运行，必须改正后才能运行
# ***异常*** 如果代码没有语法问题，可以运行，但会出运行时的错误，例如除零错误，下标越界等问题，
# 这种在运行期间检测到的错误被称为***异常***

# try-except语句   异常的捕获和处理  except 除...之外

# print(5/0)              出错会暴露文件路径
try:
	print(5 / 0)  # 异常检测
except Exception as e:  # 异常处理   Exception: 错误父类,  e: 错误对象
	print(e)  # division by zero   错误原因
# 对象打印的结果是字符串, 里面重写了__str__

# 首先执行try中的异常检测, 如果有异常, 则从上到下顺序匹配except,如果匹配成功,
# 则执行对应异常处理模块,执行完毕后不再向下匹配,直接try_except模块后继续执行

# except块从上到下的顺序, 由精确到模糊
try:
	a = [1, 2]
	print(a[3])
except IndexError as c:
	print(type(c))
	print(c, "C")
except LookupError as e:
	print(type(e))
	print(e, "Look")
except Exception as a:
	print(type(a))

print("----end------")

try:
	a = [1, 2, 3, 4]
	print(a[6])
except Exception as e:

	print("错误", e)


