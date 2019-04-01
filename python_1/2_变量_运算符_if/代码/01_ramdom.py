# 随机抽取一位同学的作业
import random    # 倒入产生随机数的模块（就是一个py文件，里面可以有很多函数和变量）

stu_list = ["易志康","张译文","曹茂新","徐明林","陈观明","胡才豪","肖誉","易云林","范益宏"]

string = random.choice(stu_list)    #随机返回列表中的一个元素
# print(string)

# 重复做相同的事情，可以用循环结构
# rang(3)--> 0 1 2，这个循环执行三次
for i in range(4):
	string = random.choice(stu_list)
	print(string)
# 将抽中的人从列表中移
	stu_list.remove(string)
