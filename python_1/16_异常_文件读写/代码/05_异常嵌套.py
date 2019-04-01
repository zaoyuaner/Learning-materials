# 类似于for in 可以嵌套
try:
	print("屌丝:周末去看大海吧!")
	raise Exception("女神:我想去逛街")
except Exception as e:
	try:
		print("屌丝: 我也没啥事,一起去逛逛")
		print("买买买")
		raise Exception("女神: 累了 回去吧")
	except Exception as e:
		print(e)
		print("屌丝: 前面有家酒店, 过去休息下")

try:
	print("我们去看大海吧")
	raise  Exception ("但是我想去逛街")
except Exception as a:
	print(a)
	try:
		print("逛街? 还不如回家撸代码")
		raise Exception ("错误")
	except Exception as e:
		print(e)
		print("我错了,逛街去吧")