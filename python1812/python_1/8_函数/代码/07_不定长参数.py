# 不定长参数*args   也要放在参数列表的最后面  是一个元组
#
def show(*args):    # 不定长参数,参数的个数可以任意个,args实际是一个列表
	# print(args)
	# print(args[0][0])    # 获取元组中的第一个列表中的第一个数
	args[0][0] = "hello"
	print(args)

# show(["a","v","b","a"])
list1 = ["a","v","b","a"]
show(list1)

def show2(num1,*args):      # 这个参数必须是一个以上
	print(num1,args)

show2(100,200,300)        # 100 (200, 300)

# 不定长关键字参数**kwargs   也要放在参数列表的最后面    是一个字典
def show1(**kwargs):   # 不定长关键字参数,个数不定,但是传参是需要使用XX=XX形式(关键字)
	print(kwargs)
	for key,value in kwargs.items():
		print(key,":",value)

# show1(10,20)          # 不能直接接值
show1(num1 = 10,num2 = 20)    # 必须使用关键字传参,否则失败
show1()                # 不定长参数可以是0个   空字典!

