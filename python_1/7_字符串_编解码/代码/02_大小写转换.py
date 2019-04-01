# 对字符串进行任何操作,都是拿返回值,自己不变

# .lower()   将所有大写转小写,非字母不处理
str2 = "Today Is a good day!"    # str2不会产生变化
str3 = str2.lower()
print(str3)

# .upper()   将所有小写转大写
str4 = str3.upper()
print(str4)
# 使用: 如果项目中需要进行不区分大小写比较,可以将整个字符串转大写再比,或者转小写再比

# .swapcase()  将字符串的大小写反转.大写变小写,小写变大写
str5 = str2.swapcase()
print(str5)

# .capitalize()   将整个字符串的第一个单词的首字母大写
str6 = "hello world"
str7 = str6.capitalize()
print(str7)       # H 变为大写,如果原本就是大写,则不变

# .title()   将一句英文每个单词的首字母大写
str8 = str2.title()
print(str8)


