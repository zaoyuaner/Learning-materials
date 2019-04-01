from  functools  import  reduce

"""
reduce(function,Iterable)  :通过函数对参数列表中的元素进行累积
function:函数
Iterable：可迭代对象，一般使用列表
工作原理：用传给reduce的function先作用于list中第一个和第二个元素，用得到的结果和list中第三个元素计算。。。
reduce(add,[a,b,c,d])
add(add(add(a,b),c),d)---->递归
"""

#需求1;求一个已知列表中元素的和
list1 = [1,2,3,4,5]
def add(x,y):
    return x + y
result1 = reduce(add,list1)
print(result1)

result2 = reduce(lambda x,y:x + y,list1)
print(result2)

#需求2：将列表[1,3,5,7,9]变换成整数13579
"""
分析：
13 = 1 * 10 + 3
135 = 13 * 10 + 5
1357 = 135 * 10 + 7
13579 = 1357 * 10 + 9
"""
list2 = [1,3,5,7,9]
def fn(x,y):
    return x * 10 + y

result3 = reduce(fn,list2)
print(result3)

#需求3：
#结合map函数，实现一个将str转换为int的函数   int()

#思路：传进来一个字符串，返回一个对应的整数
def strToInt(s):
    digits = {"0":0,"1":1,"2":2,"3":3,"4":4}
    return digits[s]

#"23401"------>23401
r0 = map(strToInt,"23401")
print(list(r0))   #[2, 3, 4, 0, 1]

r1 = reduce(fn,map(strToInt,"23401"))
print(r1)   #23401
print(type(r1))   #<class 'int'>