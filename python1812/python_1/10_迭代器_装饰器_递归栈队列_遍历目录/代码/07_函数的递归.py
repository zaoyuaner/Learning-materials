# 函数的递归: recursion 自己调自己
# count = 0
# def show():
# 	global count
# 	count +=1
# 	print("hello",count)     # count = 996崩溃 ,, 函数递归次数不超过1000次
#
# 	show()
# show()                       # 不正确的递归,没有结束条件


# 数字数列: 斐波那契数列  1 1 2 3 5 8 13 21 34 55.....
# 阶乘: 10*9*8*7*6*5*4*3*2*1
# f(n) = f(n-1) + f(n-2)     前两个数的和

def fib(count):
	if count == 1 or count == 2:    # 递归结束条件
		return 1
	else:
		result = fib(count-1) + fib(count-2)
		return result

print(fib(3))             #  2  第三个数
print(fib(5))             #  5
# print(fib(100))         # 会计算很久

# 递归优点: 逻辑清晰,易于理解
# 递归缺点: 重复调函数,效率低下

# 例: 递归求和 5+4+3+2+1
# num + fn(num-1)
def getSum(num):
	if num ==1:           # 1.递归一定要一个结束条件!
		return 1
	else:
		result = num + getSum(num -1)   # 2.递归前进条件
		return result                   # 3.递归返回
# 5 + getSum(4)   --> 5+4+3+2+1
# 4 + getSum(3)   --> 4+3+2+1
# 3 + getSum(2)   --> 3+2+1
# 2 + getSum(1)   --> 2+1
print(getSum(5))

# 汉诺塔   递归
def hanoi(n, a, b, c):
    if n == 1:
        print(a, '-->', c)
    else:
        hanoi(n - 1, a, c, b)
        print(a, '-->', c)
        hanoi(n - 1, b, a, c)
# 调用
hanoi(3, 'A', 'B', 'C')