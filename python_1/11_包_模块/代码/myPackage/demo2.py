import myPackage.demo1        # 导入其他模块是,需要使用  包名.模块名

# 导入demo1模块相当于将里面所有的代码都执行了一次.

print(myPackage.demo1.num1)   # 访问变量     包.模块.变量

myPackage.demo1.show() # 使用函数    包.模块.函数

def show():                   # 不同的模块可以使用同一个变量,同一个函数名,不会冲突
	print("helloworld")

show()