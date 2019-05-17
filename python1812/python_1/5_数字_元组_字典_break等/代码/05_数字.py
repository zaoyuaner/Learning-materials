
# 从右到左 挨个赋值
num1 = num2 = num3 =10

(num4,num5) = (3,11)    # 实质就是一个元组,元组可省略括号
print(num4)

tuple1 = num6,num7 = 10,20
print(tuple1)
print(type(tuple1))

# 变量的值交换

# 1.使用第三个变量交换
x = 3
y = 4
z = x         # 使用第三个变量接收(空杯子)
x = y         # 首尾相连即可
y = z
print(x,y)
# 2.不使用第三个变量进行交换
# 2.1使用元组(python特有)  元组的解包
y,x = x,y
print(x,y)
# 2.2使用加法
x = x + y         # 7 = 3 + 4
y = x - y         # 3 = 7 - 4
x = x - y         # 4 = 7 - 3
#2.3使用异或
x = x^y           #0011^0100 = 0111
y = x^y           #0111^0100 = 0011
x = x^y           #0111^0011 = 0100
print(x,y)

