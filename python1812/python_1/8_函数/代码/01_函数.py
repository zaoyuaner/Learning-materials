# 函数 function  函数名是函数类型的变量, 保存函数代码的地址! 函数名也是变量
# def  # define  定义   声明函数的关键字
# 函数 :1.将多次执行的代码写在一起,供重复使用,能够提高代码效率,避免重复拷贝
#      2.将功能分块,  不同的功能,不同的函数

# 2.功能分块
# 求圆的面积
def getCirclArea(r):
	print( 3.1415*r*r)
# 求圆的周长
def getCirclePerimeter(r):
	print(2*3.1415*r)
# 求矩形周长
def getRectanglePerimeter(width,heigth):
	print(2*width + 2*heigth)

# 1.函数可供重复使用,只需提供不同的参数
getCirclArea(10)
getCirclePerimeter(21)
getRectanglePerimeter(12,20)

# 为什么使用函数?
# 求一次圆的面积
import math
r = 10
result = math.pi*r**2
print(result)

r = 20                     # 第二次使用需要拷贝,所以可以封装函数
result = math.pi*r**2
print(result)

# 当你的代码需要进行多次拷贝时,就写成函数
# 函数需要接受不同的值,那么就将这个接受值得东西作为参数,其实就是变量.
def circleArea(r):
	print(math.pi * r ** 2)

circleArea(10)
circleArea(20)