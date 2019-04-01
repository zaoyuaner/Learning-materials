import itertools

#组合：从n个不同的元素中取出m个元素

result2 = itertools.combinations([1,2,3,4],3)
print(result2)
list = list(result2)
print(list)
print(len(list))

"""
4-4    1
4-3    4
4-2    6
4-1    4

组合的可能性：n! / (m! * (n -m)!)
"""