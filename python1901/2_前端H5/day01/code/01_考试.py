'''Python语言考试题分析'''


# 一， 选择题
# print(5+4j > 2-3j)
print(3 > 2 < 3)
print(('3', '2') < ('a', 'b'))
# ASCII : 1个字节表示
# 0~9：48~57
# a~z: 97~122
# A~Z: 65~90
# UTF-8 :


a,*_,c = 5,6,7,8,9
print(a, _, c)  # 5 [6, 7, 8] 9

# max = x > y ?x:y

a = [['x', 'y'], 1, 2]
b = a
c = a.copy()
a.insert(1, 3)
    # a = [['x', 'y'], 3, 1, 2]
    # b = [['x', 'y'], 3, 1, 2]
    # c = [['x', 'y'], 1, 2]
a[0].append(3)
    # a = [['x', 'y', 3], 3, 1, 2]
    # b = [['x', 'y', 3], 3, 1, 2]
    # c = [['x', 'y', 3], 1, 2]

print(b)  # [['x', 'y', 3], 3, 1, 2]
print(c)  # [['x', 'y', 3], 1, 2]


def f(x, L=[]):
    for i in range(3):
        L.append(i*i)
    print(L)

f(2)  # [0, 1]
f(3,[3,2,1])  # [3, 2, 1, 0, 1, 4]
f(3)  # [0, 1, 0, 1, 4]


def _Add(a):
    def add(b):
        return a + b
    return add

ad = _Add(1)
print(ad(1))  # 2
print(ad(2))  # 3
print(ad(3))  # 4

L = [1, 5, 3, '1', 1, 2, '3', 5, 5]
newL = list(set(map(int, L)))
print(newL)

import random
def random_color():
    L = [0,1,2,3,4,5,6,7,8,9,'A','B','C','D','E','F']
    color = '#'
    for _ in range(6):
        n = random.choice(L)
        color += str(n)
    return color

print(random_color())




