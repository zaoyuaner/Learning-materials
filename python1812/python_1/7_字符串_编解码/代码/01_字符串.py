# len() 求长度,可以作用于字符串,列表,元素,字典,集合.不能用于数字
# print(len(123))     # 报错
print(len("hello"))

# count 统计次数
string1 = "helloworld helloworld"
print(string1.count("hello"))   # 2次   统计子串在父串中出现的次数

print(string1.count("o",11,100))   # 2 分区间统计,从11到末尾的o的次数

