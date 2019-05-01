# break 直接结束整个循环,else也不会执行

for i in range(1,10):
	print(i)
	if i ==5:
		break
else:
	print("遍历结束")

# break只会结束当前所在的循环

for i in range(1,10):
	for j in range(20,31):
		print(j)
		if j ==25:
			break      # 只结束当前循环
	print(i)


