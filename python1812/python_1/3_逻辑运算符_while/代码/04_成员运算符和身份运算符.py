# in 判断这个值是否出现在列表中
list1 = [1,2,3,4,5]
print( 1 in list1 )   # 判断1这个数字是否在list1中
print( 9 in list1 )

# not in  不在列表中返回真,在列表中返回假.
print( 2 not in list1 )    # False
print( 9 not in list1 )    # True

# is : 判断两个变量内部的地址是否相同
# == : 判断两个变量指向的值是否相同

a = 10
b = a
print( id(a) )
print( id(b) )
print( a is b )     # 判断两个变量的地址是否相同

x = 20
y = 20
print( id(x) )
print( id(y) )
print( x is y )     # 因为有常量池的存在,所以使用这个常量的变量都会是同一个地址
print( x == y )

y = 100             # 给y赋值另外一个常量,地址会被修改.
print( id(x) )
print( id(y) )
print( x is y )     # 因为有常量池的存在,所以使用这个常量的变量都会是同一个地址
print( x is not y ) # True
print( x == y )     # False

# 总结: is 比较的是变量存储的地址, == 比较变量指向的值是否相等!

list2 = [1,2,3,4]    # list2指向一个对象
list3 = [1,2,3,4]    # list3指向另一个对象
print( id(list2))
print( id(list3))
print( list2 is list3)   # False
print( list2 == list3)   # True

