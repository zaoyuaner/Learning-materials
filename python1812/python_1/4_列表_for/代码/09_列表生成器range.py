# range(start,stop,step)  生成从start到stop的一个列表,不包含stop,可以用step步进
# 列表生成器
# 求50到100的和
sum = 0
for i in range(50,101):
	sum += i
print(sum)

# 求50到100的偶数和
sum = 0
for i in range(50,100,2):
	sum += i
print(sum)

# 使用枚举函数,遍历下标和元素
list1 = ["1","2","ad","第"]
for i,item in enumerate(list1):
	print("下标是:",i , "元素是:" , item)


