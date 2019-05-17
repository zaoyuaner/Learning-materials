import re

# split(pattern,string,maxsplit=0,flags=0)
#       正则表达式 字符串 切割次数    模式修正函数

# 忽略大小写,切割字符串
result = re.split(r"a","1A2a3A4a5A",flags = re.I)  # 第三个参数默认是最多切割次数,所以不能直接放修正模式,
													# 使用关键字参数即可
print(result)     # ['1', '2', '3', '4', '5', '']

str1 = "窗前明月光,疑是地上霜.举头望明月,低头思故乡."
result = re.split(r"[,.]",str1)
print(result)

# 去重拆分可能多的空格
for item in result:
	if item == "":
		result.remove(item)

print(result)

# 练习:写一个正则表达式,用来匹配手机号
#
# 1.手机号必须以1开头
#
# 2.手机号第2位只能是3,4,5,7,8,9中的一位
#
# 3.手机号总共11位数字

result = re.search(r"^1[23456789]\d{9}$","18476991129")
print(result)