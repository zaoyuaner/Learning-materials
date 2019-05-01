

# 选择14
num = 123
d = {'age':12}

def change(num, d):
    num -= 1
    d['age'] -= 1

change(num, d)

print(num, d['age'])


# 基本类型：不可变类型，boolean, str, number, tuple, None, Bytes
# 引用类型：可变类型, list, dict, set

# 赋值
# 基本类型的赋值，赋值的时候没有关联
a = 10
b = a
b = 20
print(a, b)  # 10，20

# 引用类型的赋值， 赋值的时候是有关联的
list1 = [1, 2, 3]
list2 = list1
list2[0] = 100
print(list1)  # [100, 2, 3]
print(list2)  # [100, 2, 3]

# 垃圾回收GC


# 选择15
num1 = 1 and 2        # num1 = 2
num2 = True or False  # num2 = True
result = num1*num2 + 3  # result = 2 * 1 + 3 = 5
print(result)


# 短路操作
a = 10 and None and True
print(a)  # None

b = 10 or None or True
print(b)  # 10





