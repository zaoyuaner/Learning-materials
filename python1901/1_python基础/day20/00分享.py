import requests
import pprint
from collections import Counter
url='https://www.douyu.com/gapi/rknc/directory/yzRec/2'

users = requests.get(url).json()
# print(users)
# pprint.pprint(users)

'''
判断两个字符串所用的字母及其个数都是一样的，但是它们字母的位置不一样，比如abc，bac，acb。在Python中，Counter可以解决这个问题，
'''
str1 = 'abcd12'
str2 = 'bcda21'
str4 = 'bcda23'
str3 = 'abcda'
print(Counter(str1) == Counter(str4))
print(Counter(str1) == Counter(str3))

'''
比较运算符的聚合
'''
n = 10
result = 1 < n < 20
print(result)


'''
将一个列表的元素保存到新变量中
'''
testList = [1,2,3]
x, y, z = testList

print(x, y, z)
a, b = {1:2, 3:4}
print(a, b)


'''
使用交互式“_”操作符
'''


'''
列表的转置:
    先用zip并行迭代每一个列表，然后再用map将迭代后的元组转成列表。
'''


list1=[[1,2,3,4,6],[5,6,7,8],['a','b','c','d']]
# print(zip(*list1))
# print(list(map(list,(zip(*list1)))))
print(zip(*list1))
print(list(zip(*list1)))


abfn={}

'''
Ctrl + A  : 全选
Ctrl + C  : 复制
Ctrl + V  : 粘贴
Ctrl + S  : 保存
Ctrl + X  : 剪切
Ctrl + Z  : 撤销
Ctrl + D  : 复制粘贴当前行
Ctrl + Y  : 删除当前行
Ctrl + F  : 查找
Ctrl + R  : 替换


Ctrl + Shift + V
Ctrl + Shift + E
自动换行
'''
