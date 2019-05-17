# finally 一般用于执行清理工作
try:
	print(5/0)
except Exception as e:
	print(e)
finally:
	print("无论有没有异常, 最终的都会执行finally")

print("---"*20)


try:
	list = [1,2]
	print(list[3])
	print(5/0)
	# 可以把多个错误类型使用元组抱起来,只要匹配其中一个算成功
except (ZeroDivisionError,OverflowError) as e:
	print(e)
# except 不带任何类型, 后续pass.此类写法会吞掉错误, 不作任何处理
except:
	pass

try:
	print("易志康")

except:
	pass

