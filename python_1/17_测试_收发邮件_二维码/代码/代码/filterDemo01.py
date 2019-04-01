"""
filter(function,序列)
作用：通过指定的条件过滤列表中的元素
工作原理：将传入的函数依次作用于列表中的每一个元素，根据返回的是True还是False决定元素是否需要保留
"""

#需求1：将列表中的偶数筛选出来
list1 = [1,2,3,4,5,6,7,8,9]
#作用：定义筛选的规则
def func(num):
    if num % 2 == 0:
        return  True
    return  False

result1  = filter(func,list1)
print(result1)
print(list(result1))  #[2, 4, 6, 8]

