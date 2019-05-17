
# 找出列表中出现次数最多的数,和次数
import random
list1 = [1,2,3] + [random.randint(1,10) for i in range(10)]
dict_num = {}
for item in list1:
    if item not in dict_num.keys():
        dict_num[item] = list1.count(item)
print (dict_num)
num = max(dict_num,key=dict_num.get)     # 值最大的键
print(num,"出现了", dict_num[num] , "次")

# 不基于set进行列表去重 [1,2,2,2,3,4,4,4,4]
# 删除元素时,注意这个跳过的问题
list1 = [1,4,2,2,2,2,3,3,4,4,4,4,4,]
max = 0
max_item = None
for item in list1:
    count = list1.count(item)       # 求出每个元素的次数
    if count > max:
        max = count
        max_item = item             # 既然现在找到了最多次数,那么这个item就是出现次数最多的
print("次数:",max,"元素:",max_item)

# 练习:不基于count函数 去求出出现次次数最多的元素,和次数
# 练习: 不基于set进行去重.



