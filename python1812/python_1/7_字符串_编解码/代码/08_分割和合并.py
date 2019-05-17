# 分割
# .split()   分解. 将字符串以某个特定的字符进行分割,返回一个列表
str1 = "today is a good day"
result = str1.split(" ")    # 按" " 空格来切分字符串,返回一个列表
print(result)
result = str1.split("o")    # ['t', 'day is a g', '', 'd day']


str2 = "a-b-c-d"
result = str2.split("-",2)    # ['a', 'b', 'c-d']使用最多切割次数2
print(result)

# .rsplit  从右边开始切
result = str2.rsplit("-",2)    # 从右边开始切,使用最多切割次数2
print(result)

# .splitlines()  切行
str3 = """hello
world
123
"""
   # 按照换行符(\n)切割
result = str3.splitlines()        # ['hello', 'world', '123']
print(result)
   # 参数为Ture ,留下换行符\n
result = str3.splitlines(True)    # ['hello\n', 'world\n', '123\n']
print(result)

# .join()   拼接   将可迭代对象使用某个字符进行连接 str.list.tuple.dict.set
# iterable : 可迭代对象,能够使用for in 进行遍历的对象
print("-".join(["a","b","c","d"]))   # a-b-c-d 用来拼接的列表内元素是字符串,数字不行
print("-".join(("a","b","c","d")))   # 元组
print("-".join({"a","b","c","d"}))   # 集合 无序
print("-".join("hello"))             # 字符串
print("-".join({"name":"xiaoming","age":12}))         # 字典,连接key

# 切割和拼接就是相对的操作
# 需要将字符串 a:b:c:d 中的 :改成 -
# 使用系统函数
str4 = "a:b:c:d"
list1 = str4.split(":")
print("-".join(list1))     # a-b-c-d
# 自己实现
result = ""     # 字符串无法被修改,空字符串接收
for item in str4:
# 不等于这个符号,原样添加新字符
	if item != ":":
		result += item
	else:
		result += "-"
print(result)              # a-b-c-d


# 实现字符串插入功能
str1 = "helloworld"
insert_str = "123"
insert_index = 3        # 在 3插
# 1.转列表,再插
list1 = list(str1)
list1.insert(insert_index,insert_str)
result = "".join(list1)
print(result)
# 2.切片
sub1 = str1[:insert_index]       # 0^3   hel
sub2 = str1[insert_index:]       # 3^末尾  loworld
result = sub1 + insert_str + sub2
print(result)

# 自己实现split函数
str1 = "a:b:c:d"
key = ":"
	# 使用find去查找key的下标
def mySplit(string,key):
	list1 = []
	for i in range(len(string)):
		# 分隔符存在,那么找到他的下标
		index = string.find(key)

		# 如果切割到最后一次,找不到分隔符,那么将最后一个字符加入列表,直接结束
		if index == -1:
			list1.append(string)
			break

		# 截取从0^index的子串
		sub = string[:index]

		# 将这个子串加入到列表中
		list1.append(sub)

		# 切片截取,将前面已经截取的子串去除,接着进行下一次分割
		string = string[index+len(key):]
	return list1
print(mySplit("a:b:c:d",":"))


# 自己实现join函数[1,2,3,4,5]    "-"   -- > 1-2-3-4-5
def myJoin(list1,char):
	# 列表拼接结果
	new_str = ""
	for i in range(len(list1)):   # 用下标遍历,如果用元素遍历,重复的元素也不会加char
		if i == len(list1)-1:     # 如果下标是最后一个,只加item,不加char
			new_str += str(list1[i])
		else:
			new_str += str(list1[i]) + char    # 1-2-3-4-5-  多了一个-

	# 返回拼接结果
	return new_str

list1 = [1,2,3,4,5]
print(myJoin(list1,"-"))




