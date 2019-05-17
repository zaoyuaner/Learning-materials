import random
# randint 从范围内随机一个整数,包含上下限    1=< n <=10
print(random.randint(1,10))

# choice 从序列中随机一个,不包含上限
print(random.choice(range(1,10)))

list1 = ["啊","a","e"]
print(random.choice(list1))
print(random.choice("hello"))   # 直接从hello中返回一个字符 h e l o


# random.randrange(start,end,step)
print(random.randrange(10))           # 两者等同
print(random.choice(range(1,10,2)))     # 两者等同

print(random.randrange(5,20,4))    # 求5到20的随机数,间隔要加4

# 返回一个0到1的随机数,浮点数   0<n<1
print(random.random())

# uniform  返回一个浮点数
print(random.uniform(1,19))   # 1<n<19

# shuffle  将列表内的元素随机排序.  直接修改原列表,没有返回值
list2 = ["a","b","v","d"]
random.shuffle(list2)
print(list2)


