# raise 错误
# raise + 错误类型 + ("错误原因")  raise不带参数会把错误原样抛出

try:      # 主动抛出错误
	raise ZeroDivisionError('除0错误')     # 异常处理
except ZeroDivisionError as e:
	print(e)

print("我要去拉萨")
try:
	print("我准备乘飞机过去")
	raise Exception("由于大雾，飞机不能起飞")    # raise后面的语句不会执行
	print("到拉萨了，拉萨真漂亮")
except Exception as e:
	print(e)
	try:
		print("我准备乘火车过去")
		raise Exception("由于大暴雨，铁路断了")
		print("到拉萨了，拉萨真漂亮")
	except Exception as e:
		print(e)
		print("我准备跑过去")
		print("到拉萨了，拉萨真漂亮")

