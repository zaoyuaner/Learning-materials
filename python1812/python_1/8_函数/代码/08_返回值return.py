# 如果调用函数需要得到一个结果,那么需要返回值return

def add(num1,num2):
	print(num1+num2)

add(100,200)
result = add(100,200)
print(result)             # None   如果函数没有使用return返回值,那么默认返回None


def add(num1,num2):
	return num1+num2      # 有返回值,调用函数后得到一个结果,返回的是int

result = add(100,123)
print(type(result),result)             # 返回运算后的值给result

# return 的作用
#1.调用函数返回一个值
#2.当函数执行到return,那么函数会立刻被结束,return后面的代码不会被执行的
#3.return只能使用在函数中!

def show():
	for i in range(10):
		print(i)
		if i == 5:
			return        # return强制结束函数
	print("hello")        # 不会打印hello

result = show()
print(result)             # None  如果return后面没有任何值,则返回None(默认)

# 示例
# 封装一个函数,输入一个列表,输入一个元素,查找这个元素在列表中的位置
def myFind(list1,key):
	for i in range(len(list1)):
		if list1[i] == key:        # 找到了返回下标
			return i
	return -1                   # 没找到返回-1

result = myFind([1,2,3,4],2)
print(result)                   # 1

# 总结: 函数的作用就是为了实现某个功能
# 封装: 可以将函数当一个黑盒子,只管调用,拿结果,不关注函数内部如何实现.

# 示例: 实现字符串的插入功能
def myInsert(oldString,index,insertString):
	sub1 = oldString[:index]
	sub2 = oldString[index:]
	return sub1 + "_" + insertString + "_" + sub2     # "_"  维护: 修改函数

result = myInsert("hello",3,"666")
print(result)

# 示例: #需求2：封装函数功能，判断某年是否是闰年
# > """
# > 参数：某年
# > 返回值：可设置可不设置
# > """
def isLeapYear(year):            # 如果返回是布尔值,命名加个is比较方便
	# 必须输入数字
	if type(year) == int:
		if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
			return  True
		else:
			return False
	else:
		return "输入不正确"

result = isLeapYear(12.2)
print(result)
