# 切片:提取列表中部分元素所组成的子列表,不会对原列表产生影响
# 公式: [起始:结束:步进]      从起始截取到结束,以步进为单位   包头不包尾.
#      [start:end:step]

list1 = ["a","b","c","d","e","f"]
print(list1[2])
print(list1[0:6:2])
print(list1[4:1])    # 如果end小于start,返回空列表.如果省略start,则代表从第0位开始截取
print(list1[5:100])  #"f"    不会越界,end能超出上限,代表最后一位.
print(list1[5:])  #"f"    如果省略end,取到末尾

# 切片还可以使用负数
print(list1[-4:-1])   # 从倒数第四个取到倒数第一个,不包含倒数第一个
print(list1[-1:-4])   # [] 切片默认从左到右,不能从右到左.
print(list1[:-3])     # 从0取到倒数第三个,不包含倒数第三个
print(list1[-4:])     # 从倒数第四个,取到末尾,包含末尾

# 使用step
print(list1[0:5:2])   # 从第1个取到第四个,每次取后面第二个.
print(list1[3::2])    # 从第4个取到第最后个,每次取后面第二个.

# 复制列表
list2 = list1[:]       # 省略了开始结束
print(id(list1),id(list2))    # 两个列表的内存地址不一样

# step使用负数,代表从后往前
list3 = list2[::-2]
print(list3)
print(list2)


str1 = "hello123456789"
print(str1[-1:4:-1])            # 从后往前切
print(str1[:4:-1])
