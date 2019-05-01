# 密码失败上限

# 排列组合
import itertools

# 排列
# 返回一个可迭代对象,里面包含排列的结果
# [1,2,3,4] 排列源, 1 是排列次数
result = itertools.permutations([1,2,3,4],2)      # 传一个可迭代对象,次数
for i in result:
	print(i)

# 组合   ( 元素不会重复)
result = itertools.combinations([1,2,3,4],2)
list1 = list(result)            # 将可迭代对象转列表
print(list1)

# 求笛卡尔积
# 排列组合
result = itertools.product("1234567", repeat=5)      # 字符串太多会卡死
list1 = list(result)
print(list1)
print( len(list1))      # 所有可能的次数  7**5