
from enum import Enum,IntEnum,unique

#2.
"""
enum模块：提供了Enum【类】、IntEnum【类】、unique【装饰器】
Enum【类】:通过定义一个类，继承自Enum，则该类就是一个枚举类
IntEnum【类】：通过定义一个类，继承自IntEnum，则该类就是一个枚举类,限定枚举成员只能是整数类型
unique【装饰器】：修饰一个类，则表示枚举类中的枚举成员只能是唯一的
"""
#注意1：枚举类的类名一般全部大写
#注意2:枚举中的成员本质上都是一个单例，不可实例化，不可更改，只能获取
class COLOR(Enum):
    #枚举成员/枚举常量
    RED = 0
    GREEN = 1
    BLUE = 2

#注意3：使用unique的装饰器之后，枚举成员的value必须是不可重复的
@unique
class WEEKDAY(IntEnum):
    MON = 0
    TUS = 1
    WED = 2
    #THU = "b"   #ValueError: invalid literal for int() with base 10: 'b'
    #FRI = 1     #ValueError: duplicate values found in <enum 'WEEKDAY'>: FRI -> TUS
#print(WEEKDAY.THU)

#访问枚举成员
#方式一
print(COLOR.RED)
print(type(COLOR.RED))
#方式二
red = COLOR(0)
print(red)  #COLOR.RED

#注意4：区别于普通类，枚举类的成员可以相互访问
print(red.GREEN)   #COLOR.GREEN
print(red.GREEN.BLUE.RED)  #COLOR.RED