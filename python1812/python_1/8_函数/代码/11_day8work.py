# 初级
# 1.计算从1到某个数以内所有奇数的和并返回
def getsumOdd(num):
	if num%2 == 0:                      # 2 = 2*1,    4 = 2*2,    6 = 2*3,      8 = 2*4
		return (num/2)**2               # 1 = 1**2, 1+3 = 2**2, 1+3+5 = 9 = 3**2
	else:
		return ((num-1)/2)**2 + num

result = getsumOdd(14)
print(result)          # 49 = 1+3+5+7+9+11+13

def getnum(num):
	sum = 0
	for i in range(num):
		if i%2 != 0:
			sum += i
	return sum
print(getnum(14))



# 2.判断某个数是否是偶数，返回结果
def isEveNumber(x):
	if x%2 == 0:
		return True
	else:
		return False

result = isEveNumber(100)
print(result)         # False

# 3.判断某个数是否是素数，返回结果
def isPrimeNumber(y):            # 返回真假
	if y > 1 :
		for i in range(2,y):
			if y%i==0:
				return False
    # 可以不用else  直接return
		return True

	else:
		return ("错误")

result = isPrimeNumber(151)
print(result)                 # (151, '是素数')

# 4.计算2-100之间素数的个数，返回结果
def countPrimeNumber():
	count = 0
	for i in range(2,100):
		for j in range(2,i):
			if i%j == 0:
				break
		else:
			count += 1
	return count

result = countPrimeNumber()
print(result)                  # 25

# 中级
# 1.比较某两个数的大小，返回较大的一个
def maxNum(x,y):      # 有 =  的情况！ 要单独列出来！
	if x > y:
		return x
	else:
		return y
result = maxNum(99,23)
print(result)

# 2.交换某两个变量的值
def exchange(list1):
	list1[2],list1[3] = list1[3],list1[2]
	return(list1)               # 不用返回值,只需要验证发生变化了没
list1 = [1,2,3,4]
result = exchange(list1)
print(list1)

# 高级
# 1.定义函数实现如下要求
# 	例如：输入2，5，则求2+22+222+2222+22222的和

#   2+22+222+2222+22222 = 2 x (12345) = x * (1,y+1)
def sumNum(x,y):
	list1 = []
	for i in range(1,y+1):
		list1.append(i)        # [1,2,3,4,5]
	sum = 0
	for j in list1:
		sum += j*10**(y-j)
	return sum*x
result1 = sumNum(2,5)
print(result1)

# 或   再或者看成字符串，然后转成数值相加
def sumNum2(num1,num2):
	sum1 = 0
	num3 = 0
	for i in range(num2):
		num3 += num1 * 10 ** i
		sum1 += num3
	return sum1
print(sumNum2(2,5))

# 或   定义字符串再加
def make(num,count):
	new_str = ""
	sum = 0
	for i in range(count):
		new_str += str(num)
		sum += int(new_str)
	return sum
print(make(2,5))
