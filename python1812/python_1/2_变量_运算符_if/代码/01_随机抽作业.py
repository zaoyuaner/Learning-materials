# 模块: 它就是一个py文件,里面可以有很多函数和变量
import random    #导入产生随机数的模块

#列表(数组)
stu_list = ["易云林","林涛","张译文","宋英南","曹茂新","肖誉","宗俊宇","张利耿","李文樑","徐明林",
    "易志康","陈观明","冯旭明","胡才豪","周金滔","邬秋寒","范益宏","王明眺","罗成","张兆刚","刘辛锋","龙周","尚留红"]

# random.choice()  随机返回列表中的一个元素
# string = random.choice(stu_list)
# print(string)

#重复做相同的事情,可以使用循环结构
#range(3)  ==>  0  1  2 ,        这个循环执行3次
for i in range(4):
    string = random.choice(stu_list)
    print(string)
    #将抽中这个人,从列表中移除.避免下次还抽中
    stu_list.remove(string)
