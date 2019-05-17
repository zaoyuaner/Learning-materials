# string 字符串: 由多个字符所组成的列表,但是字符串不能修改

# str 字符串类型

string1 = ""          # 空串(False),字符串支持单引号或双引号,空格也算字符
string2 = ''          # 支持多行字符串
string3 ='''          

'''                   # 换行为真,换行符

if string1:
	print("True")
else:
	print("False")
print(string1)
print(string3)

# 字符串的相加
# 因为字符串不可变,所以任何操作不会改变自身,只会返回一个结果
string6 = "hello"
string7 = "world"
string8 = string6 + string7
print(string8)

# 获取字符串中的字符
# 因为字符串本质上也是列表,所以也可以通过索引来获取列表
s4 = "asddf"
print(s4[-1])      # 可以用索引来获取字符,也会有越界问题

# 字符串的遍历和列表的遍历没有区别
# char: 字符
string = "helloworld"
for char in string:
	print(char)
# 通过下标遍历
for index in range(len(string)):
	print(string[index])
# 通过下标,字符的形式枚举遍历
for index,char in enumerate(string):
	print(index,char)

# 字符串的切片 和列表的切片没有任何区别
str2 = "acxdasdwqe"
print(str2[:4])
print(str2[::-1])

# in 判断子字符串是否在父串中
print("a" in str2)
print("acx" in str2)
print("axa" in str2)      # False 要连续的才行!

# ord()  返回ASCII码
print(ord("a"))
print(ord(" "))    # 32


