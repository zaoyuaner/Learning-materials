# and 并且  逻辑与
num1 = 0 and 3             # 3  and第一个操作数为真,那么就是后面的值
# and第一个操作数为假,那么就是前面的值 0
num3 = 1 or 1.5            # 1 or 第一个数字为假,那么就是后面的值,为真则为前面的值
num2 = True and False       # True = 1  False = 0
print(num1,num3)           # 0,1
print(num1+num2)           # 3

# 示例
print(13 % -5)       # -2  x = a + int(a/b)*b  int 取a/b的最大整数 2.6的最大整数是3
# 							x = 13 + int ( 13/5 ）*（-5） = 13-15 = -2
# 跟a的正负没有关系 -13 的结果也是-2
print(-13 % 5)
print(-13 %-5)             #-3 x = -13 + int (-13/-5) *(-5) = -13 + (-2 *-5)

# 小明要考驾照,必须满足:1,年龄是18到70之间;2,money>5000;3,不能是色盲.
age = 20
money = 4000
isBlind = True
if 18 <= age <= 70 and money >= 5000 and isBlind == False:
	print("可以考驾照")
else:
	print("不可以考驾照")
# 18 <= age <= 70  这种链式比较,python支持,会自动优化为and语句.
# 真 and 真 => 真
# 真 and 假 => 假
# 假 and 真 => 假
# 假 and 假 => 假
# 有一个假,则为假.如果有多个and,按照顺序由左到右运算.

# or  或者  逻辑或
# 小米需要去坐飞机旅游,有其中一个证件就可以坐飞机.
# 1.可以使用身份证登机;2.可以使用军官证;3.使用港澳通行证
isHaveID = True
isHaveOfficer = False
isHaveHK_ID = False
if isHaveID or isHaveHK_ID or isHaveOfficer :
	print("可以坐飞机")
# 真 or 真 =>真
# 真 or 假 =>真
# 假 or 真 =>真
# 假 or 假 =>假
# 结论:有一个真,则为真.

# not 取反  逻辑非
num = int(input("请输入一个数:"))
if not num%2:       # 如果取余num%2==1,则为True,取反则为False,进入else!
	print("是偶数")
else:
	print("是奇数")

print(not 0)

print(not 4)    # 返回布尔值False

# 短路原则
# defined定义一个函数,a是函数名,():括号中放参数.
def a():
	print("A")
	return True     # 调用这个函数,返回True

num = a()        # 调用函数  函数定义时,函数体并不会被执行.只有调用函数时,才会被执行.
print(num)       # 如果函数有return,那么调用这个函数,可以获取return的结果.

def b():
	print("B")
	return False

def c():
	print("C")
	return True

# 短路特性   and or 除外
# and短路 :如果and的前面第一个条件为假,那么后面的条件无论真假,那么该表达式的结果都会为假.
#         基于节约资源的目的,如果and前面为假,后面的表达式就不会运算了.
print(True and True and False)
if a() and a() and c():         # if后面可以进行函数调用,通过函数的调用的结果来判断真假
	print("ok")
# or短路 :如果or的第一个条件为真,那么后面的表达式无论真假,结果为真
#         基于节约资源的目的,如果and前面为真,后面的表达式就不会运算了.
print(True or False or True)       # 后面两个被短路
if a() or b() or c():              # a()返回True,or后面两个函数被短路,不会被调用.
	print("no")



