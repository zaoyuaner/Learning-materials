# 按照步骤实现下面的程序
#
# 1.让用户输入用户名、密码、工作了几个月、每月的工资（整数）
# 2.用户名或密码为空，或者工作的月数不为整数，或者月工资不为整数，则要求重新输入
# 3.如果认证成功，打印命令提示，有查询总工资，查询用户身份（如果用户名为alex则打印super
# user，如果用户名为yuanhao或者wupeiqi,则打印normaluser，其余情况均打印unkownuser），退出功能
#
# 运行效果如下：
# user: egon
# password: 123
# work_mons: 12
# salary: 10000
#
# 1查询总工资
#
# 2查询用户身份
#
# 3退出登录
#
# : 1你的总工资是: 120000.0

inPut = True
while inPut:
	user = input("请输入用户名:")
	password = input("请输入密码:")
	work_mons = input("工作了几个月:")
	salary = input("每月的工资:")
	if  user and  password  and \
		work_mons.isdigit() and \
		salary.isdigit():
		print("认证成功!")
		# print("user:", user)
		# print("password:", password)
		# print("work_mons:", work_mons)
		# print("salary:", salary)
		inPut = False
	else:
		print("请重新输入")
		inPut = True
print("————————————")
print("""1.查询总工资
2.查询用户身份
3.退出登录"""    )
print("————————————")
money = int(salary)*int(work_mons)

while True:
	menu = int(input("请选择菜单数字:"))
	if menu == 2:
		if user == "alex":
			print("super user")
		elif user == "yuanhao" or user == "wupeiqi":
			print("normal user")
		else:
			print("unknown user")
	elif menu == 1:
		salary1 = int(salary)
		work_mons1 = int(work_mons)
		print("总工资为:",money)
	elif menu == 3:
		print("退出登录")
		break
	else:
		print("请重新输入:")







