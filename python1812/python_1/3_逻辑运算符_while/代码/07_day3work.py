# 初级:
# 判断下列语句的输出结果
# 【自己判断，写出判断依据】
# 1.True and True or True         # True
# 2.True and True or False        # True
# 3.False and True or True        # False
# 4.False and True or False       # False
# 5.False and False or True       # False

# 用if语句实现下面内容:
# 1. 根据(1-7)的数值不同,打印相应星期的英文
import random
dayList = [1,2,3,4,5,6,7]
day = random.choice(dayList)
if day == 1:
	print("1 is Monday")
elif day == 2:
	print("2 is Tuesday")
elif day == 3:
	print("3 is Wednesday")
elif day == 4:
	print("4 is Thursday")
elif day == 5:
	print("5 is Friday")
elif day == 6:
	print("6 is Saturday")
elif day == 7:
	print("7 is Sunday")

# 2.假设用户名为admin，密码为123abc,从控制台分别输入用户名和密码，
# 如果和已知用户名和密码都匹配上的话，则验证成功，否则验证失败
userID = "admin"
password = "123abc"
ID = input("请输入用户名:")
answer = input("请输入密码:")
if ID == userID and answer == password:
	print("验证成功!")
else:
	print("验证失败!")

# while
# 1.计算1到1000以内所有奇数的和并输出
i = 1
sum = 0
while i <= 1000:
	if i%2:
		sum += i
		print(i," ",end="")
	i += 1
print("\n",sum)

# 2.求1-100之间可以被7整除的数的个数
num1 = 1
n = 0
print("能被7整除:")
while num1 <=100:
	if not num1 % 7:
		n +=1
		print(num1)
	num1 += 1
print("一共有",n,"个")

# 3.计算从1到100以内所有奇数的和    同1
i = 1
sum = 0
while i <= 100:
	if i%2:
		sum += i
		print(i)
	i += 1
print(sum)

# 4.计算1到100以内所有能被3或者17整除的数的和并输出
num2 = 1
sum2 = 0
while num2 <=100:
	if  not num2%3 or not num2%17 :
		sum2 += num2
		print(num2)
	num2 +=1
print(sum2)

# 5.计算1到100以内能被7或者3整除但不能同时被这两者整除的数的个数
num3 = 1
count = 0
while num3 <= 100:
	if (not num3%7 or not num3%3) and  num3 % 21:
			print(num3)
			count += 1
	num3 += 1
print("一共有:",count,"个")

# 6.计算1到500以内能被7整除但不是偶数的数的个数
num4 = 1
count1 = 0
while num4 <= 500:
	if not num4%7 and num4%2!=0:
		print(num4)
		count1 +=1
	num4 += 1
print("一共有",count1,"个")

count = 0
for i in range(1,501):
	if not i%7 and i%2:
		count +=1
print(count)

# 7.计算1到1000以内能同时被3,5,7整除的数的和并输出
num5 = 1
sum3 = 0
while num5 <= 1000:
	if not num5%3 and not num5%5 and not num5%7:
		print(num5)
		sum3 += num5
	num5 += 1
print("和为:",sum3)

# 中级
# 1.3000米长的绳子，每天减一半。问多少天这个绳子会小于5米？不考虑小数
L = 3000
day = 0
while L >=5:
	L = L //2
	day +=1
print(day)

# 2.输出100~1000以内的所有水仙花数：
#   水仙花数：一个三位数各个位上的立方之和，等于本身。
#   例如： 153 = 1（3） + 5（3）+ 3（3） = 1+125+27 = 153
num6 = 100
count2 = 0
while num6 <1000:
	if num6 == (num6//100)**3 + (num6//10%10)**3 + (num6%10)**3:
		print(num6)
		count2 += 1
	num6 += 1
print("一共有:",count2,"个")

# 3.五位数中，对称的数称为回文数，打印所有的回文数并计算个数
num7 = 10000
count3 = 0
while num7 <100000:
	if (num7//10000) == (num7%10) and (num7//1000%10) == (num7%100//10):
		print(num7)
		count3 += 1
	num7 += 1
print("回文数有:",count3,"个")

# 高级
# 打印金字塔
for i in range(5):
	print("  " * (4 - i), end="")
	print(" *  " * (i + 1))

# 空\实心正方形
for i in range(5):
	print("*  " * 5)
print()
for i in range(4):
	if i == 0:
		print("*  " * 5)
	if i == 3:
		print("*  " * 5)
		continue
	for j in range(5):
		if j == 0:
			print("*  ", end=" ")
		if j == 4:
			print("*  ")
		else:
			print("  ", end="")

# 输出9行内容,第一行输出1,第二行输出12...
# x*10+y 或者使用字符串相加
string = ""   #空字符串用于累加
for i in range(1,10):
	string += str(i)      #将数字转成字符串
	print(string)

row = 1
while row <= 9:
	i = 1
	while i <=row:
		print(i,end="")
		i +=1
	print("")
	row +=1

# 打印图形
# 1. 打印4行,2.打印空格,3.打印*
#     *
#    ***
#   *****
#  *******

i = 1
while i <=4:
	# 打印空格
	j = 1
	while j <= 4-i:         # i=1 j=1 2 3
							# i=2 j=1 2

		print(" ",end="")
		j +=1
	# 打印星
	k = 1
	while k<= 2*i-1:    # i=1 k=1
							# i=2 k=1 2 3
		print("*",end="")
		k +=1
	# 打印换行
	print("")
	i +=1









