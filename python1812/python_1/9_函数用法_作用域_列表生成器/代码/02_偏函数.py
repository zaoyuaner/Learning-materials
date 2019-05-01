# 偏函数： 对系统函数的某些参数进行固定，返回一个新函数，让原来这个函数使用更方便
#
# print( int("123"))        # 将字符串转整形
#
# print( int( "123",base= 10))     # base基于 代表进制,默认是10进制!
# print( int("123", base= 8 ))     # 83
# print( int("10010",base= 2))     # 18 二进制转10进制整数
#
# 需要多个数以二进制显示
# print( int("1001110",base= 2))
# print( int("10111010",base= 2))
# print( int("10000110",base= 2))
# print( int("100001010",base= 2))

# 偏函数的实现  将某个函数的值固定
# customInt  是对int函数的简化
# def customInt(str1,base = 2):   # 默认base值为2
# 	return int(str1,base)       # 返回一个函数int,这个base的值可以不接,使用默认值2
#
# print(customInt("10010100"))    # 使用这个函数时,就可以不再传进制了.直接使用固定值
# print(customInt("10100010"))

# 使用系统提供的函数做偏函数  partial  局部的,偏爱的
import functools        # 函数工具模块
customInt = functools.partial(int,base = 2)  # 将int函数的base值固定为2,做一个偏函数
print(customInt("10100010"))                 # 162(10进制)
