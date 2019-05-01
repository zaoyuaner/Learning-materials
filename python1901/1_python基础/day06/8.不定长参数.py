#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author：zhangjiao
print()
'''
不定长参数
当函数定义的过程中，有时候不确定用户会传递多少个参数进来，这时候
我们就可以通过不定长参数来进行处理[包裹位置参数、包裹关键字参数]
特点：能处理比声明的时候更多参数，简而言之，传递多少参数，处理多少参数
不传递，不处理。

包裹位置参数 *args
与位置参数相比定义的时候多了一个“*”
能收集除必选参数之外所有的剩余位置参数
它将收集到的参数作为元组来进行处理。

包裹关键字参数：
定义包裹关键字参数的时候：**kwargs
kwargs作为字典来进行处理的，将传递的变量名作为key，传递的值作为value。
收集除必选参数之外所有的剩余关键字参数。

若位置参数、默认参数、包裹位置参数、包裹关键字参数同时存在的情况下，
定义的顺序：位置参数、默认参数、包裹位置参数、包裹关键字参数。

'''
# print(max(1,2,3,4,5,67,87,90))
#自我介绍，介绍你的爱好d
def func4(name,age=18,*args,**kwargs):
    print(name,age,args,kwargs)

func4("lili",20,"打球","唱歌",score1=90,score=78)

def func(name,age,*hobby):
    print("我是",name,"我今年",age,"岁，我喜欢",hobby)


def func2(name,**hobby):
    print(name,"我的爱好是",hobby)

# def func3(*args,**kwargs):
#     print(args,kwargs)

func2(hobby1="吃饭",hobby2="睡觉",hobby3="敲代码",name ="lili")

# func("打游戏","吃肉","睡觉")
# func("lili",18,"吃饭","睡觉","打豆豆")

'''
求和，定义一个函数，传递多少个参数，求多少参数的和并返回。
'''
def qiuhe(*num): #num作为元组来进行处理的
    res = 0
    for x in num:
        res += x
    return res

# print(qiuhe(1,2,3,4,5))
# print(qiuhe(1,2,3,4,5,6,7,8,9))
# print(qiuhe())
'''
自己定义一个函数，实现max函数的功能.
'''
def max2(*args):
    if len(args)>0:
        maxNum = args[0]
        for x in args:
            if x>maxNum:
                maxNum = x
        return maxNum
    else:
        return None

# print(max2(1,2,3,4,5,23,45,54))
# print(max2(1,2,3,4,-5,23,-45,-54))
# print(max2())
# print(max2(1))







