#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author：zhangjiao
import random
'''
random.choice(l)
功能：从序列中随机挑选一个
random.randrange([start,]end[,step])
参数一:start 从xx开始  【可不写】默认从0开始
参数二：end 到xx结束  一定写
参数三：step 步长 间隔多少取一次 【默认1】
取值范围[start,end)

random.random()  返回一个[0,1)的浮点数
random.shuffle(list1)
功能:将列表中的元素进行随机排列

random.uniform(m,n) 功能：产生一个从[m,n]的浮点数 
'''


print(random.choice([1,2,3,4,5,6,7,8]))
print(random.choice(["lili","张三",3,4,5,6,7,8]))
print(random.randrange(0,101,2))
print(random.random())
list1 = [1,2,3,4,5,6]
print(list1)
random.shuffle(list1)
print(list1)
print(random.uniform(1,100))

