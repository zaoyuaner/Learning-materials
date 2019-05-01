#1.Python中没有原生的数据类型表示枚举
#a.字典
COLOR = {
    "RED":0,
    "GREEN":1,
    "BLUE":2,
    "YELLOW":2
}
print(COLOR["GREEN"])
COLOR["GREEN"] = 10

#b.类
class Color(object):
    #类属性
    RED = 0
    GREEN = 1
    BLUE = 2
print(Color.RED)



