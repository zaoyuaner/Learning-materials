import re

result = re.finditer("a","a1A2a3A4",re.I)
print(result)
print( next(result))
print( next(result))
print( next(result))   # finditer返回一个迭代器

# 使用正则表达式拆分
result = "1abc2def3xyz".split("2")
print(result)          # 字符串的split只能以指定字符拆分

# 以数字拆分字符串
result = re.split(r"\d","1abc2def3xyz")
print(result)      # ['', 'abc', 'def', 'xyz']

# 将一句英文,拆成每个字符串
result = "hello      world        good".split(" ")
print(result)

# \s 匹配不可见字符(空格,换行),一个
result = re.split(r"\s+","hello      world        good")
print(result)

# 替换
# replace
result = "hello".replace("l","6")    # 只能替换指定字符
print(result)         # he66o

# re.sub()(正则表达式,替换成的字符,被作用的字符)
result = re.sub("\d","-","a1b2c3d4f5g")
print(result)          # a-b-c-d-f-g  将字符串中的所有数字替换成-
result = re.subn("\d","-","a1b2c3d4f5g")
print(result)          # ('a-b-c-d-f-g', 5)  subn会返回一个元组,和替换次数


