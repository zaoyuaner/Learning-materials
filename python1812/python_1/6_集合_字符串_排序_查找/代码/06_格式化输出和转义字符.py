# 通过%来改变后面字母或者数字的含义，%被称为占位符
# > %d      整数
# > ​%f		浮点型，特点：可以指定小数点后的位数
# > ​%s		字符串

name = "xiaoming"
age = 20
money = 1000

print("name=",name,"age=",20,"money=",1000)  # 逗号会变成空格

print("name=%s,age=%s,money=%s"%(name,age,1000))

# 保留两位小数 "%.2f"%
print("%.2f"%(3.1495926))

# 需要8位字符,如果不够,前面补空格

print("%8s"%("hello"))     # 前面3个空格,一共8个字符

# 需要打印""
print("\"hello\"")    #  \" 打印"`

# \n enter换行
# \t tab
# \b backspace  按一下退格键
print("hello\nworld")
print("hello\tworld")        # 缩进
print("hello\bworld")        # 删除了一个o

# 使用字符串表示路径
path = "d:\工作\Python\03_Linux"     # 03不能打印
path = "d:\工作\Python\nomal"        # \n 会当做换行处理

# 在字符串前面加上r,会忽略转义
path = r"d:\工作\Python\03_Linux"     # 03可以打印
path = r"d:\工作\Python\nomal"
path = "d:\\工作\Python\\nomal"       # 也可以用\\








