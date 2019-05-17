#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author：zhangjiao
print()
'''
1.【递归】有5个人坐在一起，问第五个人多少岁？他说比第4个人大2岁。
问第4个人岁数，他说比第3个人大2岁。问第三个人，又说比第2人大两岁。
问第2个人，说比第一个人大两岁。最后问第一个人，他说是10岁。请问第五个人多大？
f(1) = 10
f(2) = f(1)+2
f(n) = f(n-1)+2
'''

def f(n):
    if n==1:
        return 10
    else:
        return f(n-1)+2

# print(f(5))
# print(f(20))


'''
2.一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，
求它在第10次落地时，共经过多少米？第10次反弹多高？
f(1) = 50
f(2) = f(1)/2
f(n) = f(n-1)/2
'''
def f2(n):
    if n == 1:
        return 50
    else:
        return f2(n-1)/2
print(f2(10))

res = 100
for x in range(1,11):
   res += 2*f2(x)

print(res)


'''
3.猴子吃桃问题：猴子第一天摘下若干个桃子，当即吃了一半，还不瘾，
又多吃了一个第二天早上又将剩下的桃子吃掉一半，又多吃了一个。
以后每天早上都吃了前一天剩下的一半零一个。
到第10天早上想再吃时，见只剩下一个桃子了。求第一天共摘了多少
f(1) = 1
f(2) = (f(1)+1)*2
f(n) = (f(n-1)+1)*2
'''

# def f3(n):
#     if n ==1:
#         return 1
#     else:
#         return (f3(n-1)+1)*2
#
# print(f3(10))

'''
使用队列遍历目录
'''
import collections
import os
def getAllDir(path):
    #创建一个空的队列
    queue = collections.deque()
    #将根目录添加到队列中
    queue.append(path)
    #判断队列是否为空，若不为空则进入循环
    while queue:
        #拿到路径
        path = queue.popleft()
        #列举出指定目录下所有的文件的文件名
        fileList = os.listdir(path)
        #循环遍历
        for filename in fileList:
            #拿到绝对路径
            abspath = os.path.join(path,filename)
            if os.path.isdir(abspath):
                print("目录",filename)
                queue.append(abspath)
            else:
                print("文件",filename)

path = r"E:\python\python1901"
getAllDir(path)








