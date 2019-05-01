# 设计一个程序，帮助小学生练习10以内的加法                                                           
# 详情:
#     - 随机生成加法题目;
#     - 学生查看题目并输入答案;
#     - 判别学生答题是否正确?
#     - 退出时, 统计学生答题总数,正确数量及正确率(保留两位小数点)。

import random
chance = 0        # 计数器
n = 0             # 正确次数
while chance <10:
	i = random.randint(0,10)
	j = random.randint(0,10)
	print("%d+%d="%(i,j))
	inputNum = int(input("请输入正确答案:"))
	sum = i+j
	if inputNum == sum:
		print("恭喜你,回答正确!")
		n +=1
		chance +=1
	else:
		print("很遗憾,回答错误!")
		chance +=1
	rate = (n/10)*100
print("本次测验正确率为:","%.2f"%rate,"%")



