var = 1
while var == 1:  # 表达式永远为 true
	num = int(input("输入一个数字  :"))
	print("你输入的数字是: ", num)
	break                               # 跳出循环
print("Good bye!")


# 打印10000次hello world
i = 1                       # 循环变量
while i <=1:                # i = 1 2 3 4 5
	print("hello 秀兰,啦啦啦啦")
	i += 1                  # 循环变量的自增

# 这个循环结构代码执行步骤.
# 1.设置循环变量初值
# 2.执行while判断.
#     成立: -->执行循环体-->再来执行while判断 -->成立或者不成立
#     不成立: 循环结束

j = 1
while True:
	if j >=5:
		break     # 强制跳出循环,break之后的代码不会被执行,也不会执行else.
	print("ok")
	j += 1

# 总结: 首先要创建一个循环变量,然后通过while进行判断,循环变量一定要发生变化.

# 简单的使用:
# 需求:求1-100的和
num = 1
sum = 0
while num <=100:
	sum = sum + num
	num +=1           # 循环变量的自增,一定放在循环的最后一句
print("1到100的和为:",sum)

# 打印出1到100之间所有的偶数
i = 2
while i <=100:
	if not i%2:     # 除2取余为0则为假,not为真,就打印. i%2 == 0:
		print(i)
	i +=1

# 求1到100之间的质数
num=[]
i=2
for i in range(2,100):
	j=2
	for j in range(2,i):
		if(i%j==0):
			break
	else:
		num.append(i)
print(num)
# i = 2                      错的
# while i<=100:
# 	j = 2
# 	while j <= i:
# 		if i%j ==0:
# 			j += 1
# 		break
# 	i += 1
# 	print(i)
# print([i],end="")          错的

# while else
# 当条件表达式为真，先执行完循环，最后才执行else
# 当条件表达式为假，直接执行else,
num = 1
sum = 0
while num <=100:
	sum = sum + num
	num +=1           # 循环变量的自增,一定放在循环的最后一句
else:
	print("1到100的和为:",sum)
	print("从1加到100完成")

# 使用break可以有效地减少无用循环
count = 1
while count <= 10:
	if count ==5:
		break
	print("helloworld")
	count +=1
else:
	print("打印完成")

# 计算10的阶乘:     10*9*8*7*6*5*4*3*2*1
num = 10
total = 1
while num >=1:
	total *=num
	num -=1
print("10的阶乘为:",total)


# 统计100-1000之间能被6整除的数的个数
count = 0        # 计数器
num = 100        #循环变量
while num <=1000:
	if not num%6 :
		count += 1
	num += 1
print(count)



