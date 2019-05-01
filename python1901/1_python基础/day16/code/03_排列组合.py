
# 排列  1,2,3 : 123,132,213,231,312,321
# 组合  1,2,3 : 111,112,113,121,...

import itertools

# 排列
res = itertools.permutations([1,2,3], 3)
# print(res)  # <itertools.permutations object at 0x00000266BD109048>
# print(list(res))  # [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]

# 组合
res = itertools.combinations([1,2,3,4], 3)
# print(list(res))  # [(1, 2, 3), (1, 2, 4), (1, 3, 4), (2, 3, 4)]

# 笛卡尔积
res = itertools.product('0123456789abcdefghijklmnopqrstuvwxyz', repeat=3)
list1 = list(res)
print(list1)
print(len(list1))

list2 = (item for item in res)
with open('pwd.txt', 'a') as fp:
    for item in list2:
        fp.write(''.join(item) + '\n')





