# 1.必须参数: 形参的个数和实参的个数必须严格一一对应
def add(num1,num2):
	print(num1,num2)

# add(10)    错误,必须一一对应

add(10,23)
add(num1= 10,num2= 12)  # 关键字参数  使用形参=值得形式,传参 {key:value}
add(num2= 10,num1= 23)  # 因为有=的存在,所以使用关键字参数,可以不按照声明顺序传参

# 如果关键字参数只有一个,那么必须放到参数列表的最末尾
add(10,num2=20)        # 合法
# add(10,num1=10)        # 不合法 num1已经传参
# add(num1=10,2)         # 不合法

# 2.系统关键字参数
print("hello",end=":")   # end= 打印之后以:结尾
print("world")

# 3.默认参数: 如果形参没有接收到值,可以使用默认值
# 如果调用add函数时,num1num2没有接收到值,那么使用默认值,
# 如果接收到了,那就是用接收到的值
def add(num1=10,num2=20):
	print(num1 + num2)

add()      # num1 num2 都是用备选项
add(100)   # num1=100,num2使用默认值
add(100,200)  # 都接收到值,那么默认值不用

# 和关键字一样,如果只有一个默认参数,需要写在后面
def add(num1,num2=100):
	print(num1+num2)
add(10)

