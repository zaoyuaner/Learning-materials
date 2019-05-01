# 生成器: 允许使用next()一步一步的遍历方式.生成器遍历完一次后不能再遍历第二次
# 只能遍历一次!

# 1.第一种创建方式  ()使用小括号
result = (i**2 for i in range(1,6))
print(result)          # 生成器类型(相较于元组,字符串,数字)<generator object <genexpr> at 0x103318b10>

print(next(result))    # 1  分步遍历,每次调用next都是遍历生成器的一次操作
print(next(result))    # 4
print(next(result))    # 9
print(next(result))    # 16
print(next(result))    # 25
# print(next(result))  # 遍历完,再遍历就会崩溃

for item in result:    # 遍历空了之后没有输出结果,result空了,不会进入for循环.
	print("6666")
	print(item)        # 无值!

# 2.第二种创建方式  yield 退步
# 只要函数使用了yield关键字,他就是生成器
def test():
	for i in range(1,6):
		print(i**2)
		yield           # 让步 .执行到yield的时候，则函数会停止，将yield后面的变量返回
		print("hello")  # 这句话会在下一次的next执行

result = test()         # 接收函数调用的结果,这个结果是一个生成器
print(result)           # <generator object test at 0x101c56048>
next(result)            # 1 输出生成器需要用next
next(result)            # hello 4
next(result)            # hello 9
next(result)            # hello 16
next(result)            # hello 25
# next(result)            # StopIteration  没了

# 用for in遍历
for item in result:     # item是生成器类型
	item                # for item 就相当于走了next

