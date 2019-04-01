# def 函数名(num1,num2,num3):   遵循标识符命名规则,不能数字开头等等
#    函数体(pass)
def test(num1,num2,num3):
	pass


# 1.无参无返回值的函数
def show():
	print("天秀")

show()            # 函数名加()  直接调用

# 函数声明时,内部代码不会被执行,只有函数被调用时,内部代码才会执行!

# 函数如果同名,按照顺序结构,后面的函数会覆盖前面的函数

# python不支持先调用再声明,javascript支持
def show():
	print("秀儿,是你吗!")

show()           # 覆盖前面的show的"天秀"