# str() 将参数转为字符串类型,支持所有类型

result = str(123)
print(result)
print(type(result))
print(type(str([1,2,3,4,5])))   # 字符串形式的列表
# 因为变量在内存中,就是一个地址,那么在与前端交互时,是无法传递整个地址的,
# 所以都是将变量转换为字符串的,再传递

# 字符串也可以转数字
print(int("100"))          # 100

# 字符串转列表
print(list("hello"))       # ['h', 'e', 'l', 'l', 'o']
                           # 根据这个原理,可以将字符串排序!
# 字符串转元组
print(tuple("hello"))      #  ('h', 'e', 'l', 'l', 'o')

# 字符串转字典
dict(hello = "helloworld")  # 能转字典,需用=形式,前为不可变类型

# 字符串转集合
print(set("hello"))        # {'e', 'o', 'h', 'l'} 去重了,无序


