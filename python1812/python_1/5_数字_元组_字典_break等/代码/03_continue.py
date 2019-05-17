# continue   结束本次循环,直接进行下次循环


for i in range(10):
	if i ==5:
		continue         # 结束本次循环,不执行print,没有打出5
	print(i)


# 求列表中所有数字的和
list1 = [1,2,"我","good",10]
sum = 0
for item in list1:
	if type(item)!= int:  # 如果这元素的类型不是数字,直接跳过
		continue
	sum +=item
print(sum)