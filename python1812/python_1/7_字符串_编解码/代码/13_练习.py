
# 把"hello world123"转成大写
str1 = "hello 123world123"
print(str1.upper())

# 用遍历的方法,解释upper()
str2 = ""
for char in str1:
	if char.isalpha():         # if 97<=code(char)=<122: a^z 用ascii码范围限定
		str2 +=chr(ord(char)-32)   # 获取字符的ASCII码-32,转换成大写,转换成字符串输出
	else:
		str2 +=char
print(str2)

# 需求:统计下面字符串中每个单词的出现次数,生成一个字典,单词为key,次数为value
str3 = "hello world today is a good day hello world"
	# 1.将这个字符串拆成单词列表
list1 = str3.split(" ")
print(str3)

dict1 = {}
for item in list1:
	dict1[item] = list1.count(item)    # 单词用列表计数,字母用str1计数
print(dict1)

# 需求: 输入一个时间,输出下一秒
# 例:12:23:33   输出 12:22:24
# 1.需要考虑到进位的问题,将时间进行拆分
time = input("请输入时间:")

list2 = time.split(":")        # 用冒号拆分
	# 使用input接收的全是字符串,需要转换为int
hour = int( list2[0] )
minute = int( list2[1] )
second = int( list2[2] )

second += 1
if second == 60:
	#秒归零,分钟进位
	second = 0
	minute +=1
	if minute == 60:
		#分钟归零,小时进位
		minute = 0
		hour +=1
		if hour == 24:
			#小时归零
			hour = 0
print("%02d:%02d:%02d"%(hour,minute,second))   # %02d 整数有两位,不足补0

# 实现字符串在某个位置插入字符串的功能
str5 = "hello"
place = int(input("请输入想插入字符串的位置下标:"))




# 实现join函数
str4 = "a:b:c:d"
result = ""     # 字符串无法被修改,空字符串接收
for item in str4:
# 不等于这个符号,原样添加新字符
	if item != ":":
		result += item
	else:
		result += "-"
print(result)              # a-b-c-d



