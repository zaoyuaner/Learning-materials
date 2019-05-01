import re

# [] 表示单个字符范围
# {} 表示前面字符出现的次数
# () 表示整体，表示分组

string = '0755-88888888'
pattern = '(\d{4})-(\d{8})'
# pattern = '(\d{4})-(?:\d{8})'  # ?：非捕获性分组

res = re.search(pattern, string)
# print(res)
# group: 获取分组的内容
# print(res.group())  # 0755-88888888
# print(res.group(0))  # 0755-88888888
# print(res.group(1))  # 0755 获取第一个分组（第一个括号）中匹配的内容
# print(res.group(2))  # 88888888 获取第二个分组的内容

print(res.groups())  # 获取所有分组的内容，得到元组

# pattern = '\d{4}-\d{8}'
# res = re.findall(pattern, string)
# print(res)

# 分组别名
string = '0755-88888888'
pattern = '(?P<CityCode>\d{4})-(?P<phone>\d{8})'
res = re.search(pattern, string)
print(res.group('CityCode'))  # 0755
print(res.group('phone'))  # 88888888












