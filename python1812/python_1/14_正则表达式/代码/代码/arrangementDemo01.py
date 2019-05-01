import  itertools

#1。排列
#从n个不同的元素中取出m（m <= n）个元素,按照一定的顺序排成一列
#m == n,全排列(permutations)
#参数：可迭代对象 ，  个数
"""
1 ,2 ,3
123
321
231
312
...
"""

result1 = itertools.permutations([1,2,3,4],1)
print(result1)
list = list(result1)
print(list)
print(len(list))

"""
总结：
4 -1   4
4-2    12
4-3     24
4-4     24

排列的可能性：n! / (n-m)!
"""

