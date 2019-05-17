
# 1.求1-100之间能被7整除的数的个数
count = 0
for i in range(1,101):
	if not i %7:
		count += 1
		print(i,end=" ")
print("\n","个数为:",count)

# 2.计算1到100以内的所有奇数的和
sum = 0
i = 1
for i in range(1,101,2):
	print(i,end=" ")
	sum += i
print("\n","和为:",sum)

# 3.计算从1-100以内所有能被3或者17整除的数的和
sum = 0
for i in range(1,101):
	if not i%3 or not i%17:
		sum += i
		print(i,end=" ")
print("\n","和为:",sum)

# 4.计算1到100以内能被7或者3整除但不能同时被这两者整除的数的个数
count = 0
for i in range(1,101):
	if (not i%7 or not i%3) and i%21:
		count +=1
print(count)

# 5.计算1到500以内能被7整除但不是偶数的数的个数
count = 0
for i in range(1,500):
	if not i%7 and i%2:
		count +=1
print(count)

# 中级
# 1.从键盘输入一个数n,判断是不是一个质数
num = int( input("请输入一个数:"))
if num >=2:
	for i in range(2,num):
		if not num%i :
			print(num,"不是质数")
			break
	else:
		print(num,"是质数")
else:
	print("输入错误!")

# num = int( input("请输入一个数:"))
# isPrime = True
# if num>2:
# 	for i in range(2,num):
# 		if  num%i == 0:
# 			isPrime = False
#           break
# 	if isPrime:
# 		print("质数")
# 	else:
# 		print("合数")
# else:
# 	print("输入错误!")

# 2.求1000以内的水仙花数
for i in range(100,1000):
	if i == (i//100)**3 + (i//10%10)**3 + (i%10)**3:
		print(i)

# 3.求2-100之内的素数.
for num in range(2,101):
	for i in range(2, num):
		if not num % i:
			break
	else:
		print(num,end=" ")
print("是素数")

# 4.优化猜数字游戏
# 计算机出一个1~100之间的随机数由人来猜
# 	 计算机根据人猜的数字分别给出提示大一点/小一点/猜对了，
# 这个过程可以循环进行，当进行5次以上还猜不对的话，则打印：
# 智商余额不足
import random
count = 0
while True:
	guessNum = int( input("请猜一个数字:"))
	i = random.randint(1,100)        # random.choice(range(1,100))  1-99
	randomNum = i
	if count == 5:                   # for count in range(10):
		print("智商余额不足")
		break
	if guessNum > i :
		print("小一点!")
		print("随机的数为:", randomNum)
		count +=1
	elif guessNum < i:
		print("大一点!")
		print("随机的数为:", randomNum)
		count +=1
	else:
		print("猜对啦!")


# num = random.randint(1,100)
# print(num)
# for i in range(1,5):
# 	myInput = int(input("请猜一个数:"))
# 	import random

	# # num = random.choice(range(1,100))   #1~99
	# num = random.randint(1, 100)  # 1~100
	# print(num)
	# for i in range(5):
	# 	myInput = int(input("请输入一个数:"))
	# 	if myInput == num:
	# 		print("猜对了")
	# 		break  # 执行break,for后面的else不会被执行
	# 	elif myInput < num:
	# 		print("大一点")
	# 	else:
	# 		print("小一点")
	# else:
	# 	print("智商余额不足")

