# 初级
# 1.已知字符串：“this is a test of Python”
# 	a.统计该字符串中字母s出现的次数
str1 = "this is a test of Python"
count_s = str1.count("s")
print(count_s)

# 	b.取出子字符串“test”
str2 = str1.split(" ")
print(str2[3])

index = str1.find("test")     # 找到test的下标
print(str1[index:index+len("test")])    # 切片加字符串长度

# 	c.采用不同的方式将字符串倒序输出
# (a) 切片
print(str1[::-1])
# (b) 先转列表,在调用reverse,再转字符串
list1 = list(str1)
list1.reverse()
print(list1)
print("".join(list1))
# (c) 遍历字符串,从后往前遍历
new_str = ""
for i in range(len(str1)-1,-1,-1):         # range(10,-1,-1)  步长为负,开始可以大于结束  到0
	new_str += str1[i]
print(new_str)

# 	d.将其中的"test"替换为"exam"
print(str1.replace("test","exam"))

# 2..已知字符串 a = "aAsmr3idd4bgs7Dlsf9eAF",要求如下
# 	a.请将a字符串的大写改为小写，小写改为大写    # .swapcase 大写转小写,小写转大写
a = "aAsmr3idd4bgs7Dlsf9eAF"
c = a.swapcase()                           # 使用系统函数
b = ""
for char in a:       # 或者 "a" <=char <= "z"  也可以
	if 97<= ord(char) <=122:             # 小写字母的ASCII阈值 97,97+26-1
		char = chr(ord(char)-32)
		b +=char
	elif 65<= ord(char) <=90:            # 大写字母的ASCII阈值 65,65+26-1
		char = chr(ord(char)+32)
		b +=char
	else:
		b +=char
print(b,type(b))
print(c)

# 	b.请将a字符串的数字取出，并输出成一个新的字符串
c = ""
for char in a :                         # if isdigit 判断是不是数字
	if 48<=ord(char)<=57:  # if char.isdigit():  # 数字的ASCII阈值   48,48+10-1
		c +=char
print(c,type(c))

# 	c.请统计a字符串出现的每个字母的出现次数（忽略大小写，a与A是同一个字母），并输出成一个字典。 例 {'a':4,'b':2}
d = a.lower()                    # 全部转小写
dict1 = {}
for char in d:
	if char.isalpha():           # 判断是不是字母
		if char not in dict1:    # 将写入字典的次数减少到1次
			dict1[char] = d.count(char)        # 字母做键,次数做值
print(dict1)

# 	d.输出a字符串出现频率最高的字母

dict2 = {}
for char in a:
	dict2[char] = a.count(char)
print(dict2)
max_index = 0
key_max = None
for key,value in dict2.items():
	if value > max_index:
		max_index = value
		key_max = key
print(key_max)

max = 0
max_char = ""
for char in a:
	if char.isalpha():           # 只统计字母
		count = a.count(char)
		if count > max:
			max = count
			max_char = char      # 当前次数就是最多次,那么这个字符就是最多字符
print("次数:%d,字符:%s"%(max,max_char))


# 	e.请判断 'boy'里出现的每一个字母，是否都出现在a字符串里。如果出现，则输出True，否则，则输 出False
#   continue 后面无法执行语句,可采用布尔值判断!
str1 ="boy"
isIn = False
a = "aAsmr3idd4bgs7Dlsf9eAF"
for char1 in str1:
	if char1 in a :
		isIn = True             # 可以不用continue
	else:
		isIn = False
		break
if isIn :
	print(True)
else:
	print(False)

str2 = "asm"
for char in str2:
	if char not in a:        # 遍历不在就输出False
		print(False)
		break                # 直接结束循环,包括else
else:
	print(True)              # 遍历结束,都没有打印False,代表都在,所以可以输出True

# 1.去除字符串两端的指定字符
str1 = "******hello****world***"
print(str1.strip("*"))          # 系统函数

#  从0开始判断,这个字符是不是*,是*就count+1,然后切片
#  除去前面的*
count = 0
key = "*"
for i in range(len(str1)):
	# 是*,计数器就增加
	if str1[i] == key:
		count += 1
	else:
		# 不是,就立刻结束
		break
str1 = str1[count:]     # 切片,从count切到最末尾
print(str1)

#  除去后面的*
count = 0
for i in range(len(str1)-1,-1,-1):      # range(10,-1,-1): 从10遍历到0
	if str1[i] ==key:
		count += 1
	else:
		break
str1 = str1[:len(str1)-count]           # 切片到长度减计数
print(str1)

# 2.键盘输入一句英文 将每个单词的首字母大写
# 	例如:
# 		输入: hello nice to meet you
# 		转化之后:Hello Nice To Meet You
a = "hello nice to meet you"
print(a.title())
#   或者先拆分,再转每个元素的第一个字母,再用join加空格拼接
import re

def myTitle(str1):
	# 将字符串拆分,然后遍历,将每个单词首字母大写.capitalize()
	list2 = []
	# list1 = str1.split(" ")
	list1 = re.split(r"\s+",str1)          # 正则表达式的应用,去除重复的空格,只去除一个则去掉+
	print(list1)
	for item in list1:
		# 将每个单词首字母大写
		result = item.capitalize()
		# 使用一个空列表,将转换后的单词接收起来
		list2.append(result)
	# 将转换后的结果,通过空格拼接,再返回
	return  " ".join(list2)

str1 = "hello nice to meet you"
print( myTitle(str1))

#
# 3.输入一个字符串，压缩字符串如下aabbbccccd变成a2b3c4d1
#    逻辑: 将字符做键,次数做值,转为字典,再将字典转为字符串
def change(string):
	dict1 = {}
	for char in string:
		if char not in dict1:
			dict1[char] = string.count(char)
	# 遍历这个字典,将键值加起来
	new_string = ""
	for key,value in dict1.items():
		new_string += str(key) + str(value)
	return new_string

print(change("aabbbccccd"))

#   先创建一个空字符串,遍历需压缩的字符,如果不在空字符串中,添加进去,再添加count.

# 4.完成猜拳游戏
# 		-----------------------------
#
# 		1. 石头
# 		2. 剪刀
# 		3. 布
#       请输入你的选择:
# 		-----------------------------
# 		你的选择是【布】, 电脑的选择是【石头】
# 		恭喜你获得了胜利！
import random

list1 = ["1.石头","2.剪刀","3.布"]

while True:            # 给出个死循环,知道赢过电脑,才推出
	computer_choice = random.choice(list1)
	print(computer_choice)

	print("-----------------")
	for item in list1:
		print(item)
	print("-----------------")
	myChioce = input("请输入你的选择:")
	if "1" <= myChioce <= "3":
		# 获取电脑选择元素的下标
		c_index = list1.index(computer_choice)
		# 获取我选择的下标   因为选择1实际是第0个
		my_index = int(myChioce) - 1

		# 例外情况  布(list1[2])大于石头(list1[0])
		if my_index == 2 and c_index == 0:
			print("你选择了%s,电脑选择了%s" % ((list1[my_index]), list1[c_index]))
			print("恭喜你获得了胜利")

		# 例外情况2  石头(list1[0])小于布(list1[2])
		if my_index == 0 and c_index == 2:
			print("你选择了%s,电脑选择了%s" % ((list1[my_index]), list1[c_index]))
			print("你输了!")

		# 正常判断,小下标 > 大下标,代表赢了
		elif my_index < c_index:
			print("你选择了%s,电脑选择了%s"%((list1[my_index]),list1[c_index]))
			print("恭喜你获得了胜利")
			break
		elif my_index > c_index:
			print("你选择了%s,电脑选择了%s"%((list1[my_index]),list1[c_index]))
			print("菜鸡,你输了!")
		else:
			print("平局")

	else:
		print("选择不正确,请重新选择")

