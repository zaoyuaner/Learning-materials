print(abs(-7))     # 求绝对值

# max函数支持两种参数,一种是一个可迭代对象(列表),一种是放多个参数.
print(max(3,7,9))
list1 = [5,10,6]
print(max(list1))

print(min(1,3,5,7,89,33))
print(min(list1))

# pow == x**y  求指数
print(pow(2,3))

# round  四舍五入 (数字,保留位数)   不建议使用,一般使用ceil floor
print(round(3.1415))
print(round(3.891))
print(round(3.675,2))      # 小数在计算机中存储是无理数,无限位的,可以理解为5舍6入
print(round(1.899,2))      # 0被省略

import math
print(math.ceil(3.7))      # 天花板,向上取整:求大于该数的最小整数
print(math.floor(3.7))     # 地板,向下取整:求小于该数的最大整数

print(math.sqrt(16))       # 开平方

print(math.modf(34.12))    # 将这个数转成元组的形式(小数,整数)