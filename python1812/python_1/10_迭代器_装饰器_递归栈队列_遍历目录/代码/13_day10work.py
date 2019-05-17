# 1.使用递归实现：计算某个数的阶乘
def fac(num):
	if num == 1:
		return 1
	else:
		result = num * fac(num-1)
		return result
print(fac(10))                 # 3628800


# 2.定义函数实现如下要求
# 例如：输入2，5，则求2 + 22 + 222 + 2222 + 22222 的和
# 当做字符串,5变4,4变3,3变2  切片
def rec(str1):          #  recursion
	if len(str1)== 1:       # 如果只有一个2 那么直接返回这个2
		return str1
	else:
		result = int(str1) +int (rec( str1[1:]) )          # 22222 + rec(2222)
		return result

def getSum(num,count):
	return rec( str(num)* count )      # 用字符串"2"*5

print( getSum(2,5) )