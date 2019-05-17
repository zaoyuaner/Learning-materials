# else 用法
try:
	print("ok")              # 没有异常的话,会执行else
except Exception as a:
	print(a)
else:
	print("如果没有异常会走else,有异常不走else")
	print("else是可选的")

print("________")