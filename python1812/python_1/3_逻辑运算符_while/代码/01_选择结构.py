x = 'runoob'
for i in range(len(x)):
	print(i,x,x[i])
print(len(x))

day = int( input("请输入星期：") )

if 0<day<8:
	if day == 1:
		print("周一")
	elif day == 2:
		print("周二")
	elif day == 3:
		print("周三")
	elif day == 4:
		print("周四")
	elif day == 5:
		print("周五")
	elif day == 6:
		print("周六")
	else:
		print("周日")
else:
	print("输入错误")

# 从键盘输入三个数，求出最大数.最小数
num1 = int(input("第一个数:"))
num2 = int(input("第二个数:"))
num3 = int(input("第三个数:"))
max = num1
min = num1
if num2 > max:
	max = num2
if num3 > max:
	max = num3

if num2 < min:
	min = num2
if num3 < min:
	min = num3
print("最大数:",max,"最小数:",min)

