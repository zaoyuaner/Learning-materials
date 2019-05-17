x = 3
y = 4
print(" x*y = ", x*y )     # 打印时带上前缀

# 从键盘接受值，input会让程序暂停
num = input("请输入一个数：")
print(type(num))
num = float(num)      # 将字符串转数字,整数可用int，但会丢弃小数位。
print( num + 100)     # 不支持字符串加数字，只支持字符串加字符串或者数字加数字。

print( int(4.66) )    # 转整数，会丢弃小数位

# 示例：输入长、宽、求面积
# 如果代码出现函数的嵌套调用，最先调用的是内层函数，然后调用外层函数。
width = int(  input("请输入宽度：")  )
length = int(  input("请输入长度：")  )
print("面积是：",width * length)

# str()    将参数转字符串
# int()    将参数转整数
# float()  将参数转浮点数
print( str(100) )
print( type(str(100)) )

print( int(3.1415) )
print( int("100") )    # 100
# print( int("a") )    #转换非数字，会崩溃

#实际工作中，需要先对字符串校验，在进行转换，避免转换失败造成程序崩溃
if "aaa".isdigit():     # 判断是不是数字类型字符串
	print("yes")
else:
	print("no")
