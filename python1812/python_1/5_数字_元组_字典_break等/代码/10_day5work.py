# 1.自定义一个数字列表,获取这个列表的最小值,并将列表转化为元组
import random
list1 = [random.randint(1,50) for item in range(10)]
tuple1 = tuple(list1)
print(list1)
min = list1[0]                  # 找最小数,不能直接给0
for i in list1:
	if i < min:
		min = i
print("最小值为:",min)
print("转换为元组为:",tuple1)

# 2。自定义一个数字列表，元素为10个，找出列表中最大数连通下标一起输出
list2 = [random.randint(1,100) for item in range(10)]
print(list2)
max = list2[0]
max_index = 0
for i in list2:          # for i in range(len(list2)  i就是下标
	if i > max:
		max = i
print("最大的值为:",max,"其下标为:",list2.index(max))

# for index,item in enumerate(list2):       # 枚举法也可行
# 	if max < item:
# 		max = item
# 		max_index = index
# print(max,max_index)


# 3.自定义一个数字列表,求列表中第二大数的下标
list3 = [random.randint(1,100) for item in range(10)]
print(list3)
max1 = list3[0]
for i in list3:
	if i > max1:
		max1 = i           # 找出最大值
sub = list3.index(max1)    # 最大值的下标
# print(type(sub))
max1_num = list3.pop(sub)    # 取出最大值
print(list3)

max2 = list3[0]            # 可以浅复制一个列表,找出第二大的数,再在原列表中找下标
# print(max2)
for j in list3:
	if j > max2:
		max2 = j           # 找出新列表中的最大值
list3.insert(sub,max1_num)   # 补回原最大值,insert没有返回值!用变量接收为False
sub2 = list3.index(max2)
print(list3)
print("第二大的数为:",max2)

# 4.B哥去参加青年歌手大奖赛,有10个评委打分,(去掉一个最高分一个最低分)求平均分
list5 = [random.randint(1,100) for item in range(10)]
print(list5)
max3 = list5[0]
min3 = list5[0]
# print(max3)
for i in list5:
	if i > max3:
		max3 = i
	if i < min3:
		min3 = i
print(max3)              # 最高分
print(min3)              # 最低分
list5.remove(max3)
list5.remove(min3)
print(list5)
print("去掉一个最高分,去掉一个最低分,所得平均分为:",sum(list5)/len(list5))

# 5.定义元组，存放5个学生的成绩【成绩值自己设定】，获得成绩之和，平均成绩，最小成绩，最大成绩。
tuple1 = (68,90,89,95,59)
sum = 0
min_score = tuple1[0]
for i in tuple1:
	sum +=i
	if i < min_score:
		min_score = i
max_score = tuple1[0]
for j in tuple1:
	if j > max_score:
		max_score = j
print("成绩之和为:",sum,"平均成绩为:",sum/5,"最小成绩为:",min_score,"最大成绩为:",max_score)

# 6.已知列表list = [34,55,67,88,99,100],使用二分法查找67在列表中的位置

# 练习
# 不基于count函数,去求出出现次数最多的元素,和次数
# list11 = [1,1,1,1,2,2,3,4,4,5,6,8]
# list12 = []
# count = 0
# for i in list11:
# 	if i not in list12:
# 		list12.append(i)
# print(list12)
# for j in list11:
# 	for l in list1
# 				print(j)
# 基于比较来获取最多次数
# 实现的逻辑.拿列表中第0个元素去和后面的每个元素进行比较,如果相等,则计数器加1
# 使用一个max变量接收最大次数
# 使用一个max_item接收最多次数元素
list1 = [1,5,5,5,5,5,5,4,4,3,3,3]
max = 0
max_item = None
for i in range(len(list1)):
	count = 0          # 第一次比完1之后,第二次比5,计数器归零
	for j in range(i,len(list1)):  # 当i=0  j= 0 1 5 5 5 5 ...
		if list1[i] == list1[j]:
			count +=1

			if count > max:
				max = count
				max_item = list1[i]
print("最多次数:",max,"做多次数字符:",max_item)

# 不基于set进行列表去重[1, 2, 2, 2, 4, 4, 4, 4]
# 删除元素时, 注意这个跳过的问题
list9 = [1,2,2,2,4,4,4,4]
list10 = []
for i in list9:
	if i not in list10:
		list10.append(i)
list9 = list10
print(list9)

# 或者
list9 = [1,2,2,2,4,4,4,4]
i = 0
while i < len(list9):       # 用for可能会出现越界!
	j = i+1
	while j <len(list9):
		if list9[i] == list9[j]:
			del list9[j]
			continue             # 删除后下标不要加1,继续进行下一次比较!
		j +=1
	i +=1
print(list9)

# 求出现最多次数的元素
# list3 = [1,2,2,2,2,5,5,7,7,7,7,7,7,7,7]
# dict1 = {}
list3 = [1,2,2,2,2,5,5,7,7,7,7,7,7,7,7]
dict_num = {}
for item in list3:
	if item not in dict_num.keys():
		dict_num[item] = list3.count(item)
print (dict_num)
num2 = max(dict_num,key=dict_num.get)     # 值最大的键   比较值for key,item in dict1.items():
print(num2,"出现了", dict_num[num2] , "次")

# max = 0
# max_item =None
# for key,value in dict1.items():
#   if value>max:
#         max = value
#         max_item = key

# 中级
# 1.将一个列表逆序输出
import random
list6 = [random.randint(1,100) for item in range(10)]
print(list6)
list6.reverse()
print(list6)
print(list6[::-1])             # 切片

list2 = []
for item in list6:
	list2.insert(0,item)       # 定义一个空列表,一直往空列表的第0个元素插入
print(list2)

list1 = []
for i in range(len(list1)//2):      # 交换次数除以2
	list1[i],list1[-i-1] = list1[-i-1],list1[i]    # 交换

# 2.输入某年某月某日,判断这一天是这一年的第几天
# year = int(input("请输入年:"))
# month = int(input("请输入月:"))
# day = int(input("请输入日:"))
# if not year%4 and year%100:
# 	if not month%2:
# 		sum1 = month/2*30 + month/2*31 +day
# 		print(sum1)
# 	else:
# 		sum2 = month/2*30 + (month-(month/2))*31 +day
# 		print(sum2)

dat = input("请输入某年某月某日，格式为 yyyy-mm-dd ：")
# print(dat)
y = int(input("请输入年:"))
m = int(input("请输入月:"))
d = int(input("请输入日:"))
# print(y,m,d)
ly = False
if y%100 == 0:  #若年份能被100整除       # if (y%4 == 0 and y%100 ==0)or y%400 ==0
	if y%400 == 0:  #且能被400整除      #  月数减1,day累加
		ly = True  #则是闰年
	else:
		ly = False
elif y%4 == 0:  #其它情况下，若能被4整除
	ly = True  #则为闰年
else:
	ly = False

if ly == True:  #若为闰年，则2月份有29天
	ms = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
else:
	ms = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

days = 0
for i in range(1, 13):  #从1到12逐一判断，以确定月份
	if i == m:
		for j in range(i-1):  #确定月份i之后，则将ms列表中的前i-1项相加
			days += ms[j]
print('%s是该年份的第%s天。' % (dat, (days + d))) #最后再加上“日”，即是答案

# 3.给定一个列表：将列表中指定的某个元素全部删除
list8 = [1,1,2,3,4,231,112,33,1,1,1,1,"a",2]
count = list8.count(1)
# 删除1
for i in range(count):
	list8.remove(1)
print(list8)


# 4.自定义一个列表,最大的与第一个元素交换,最小的与最后一个元素交换,输出数组
list7 = [78, 45, 43, 6, 59, 70, 57, 93, 32, 89]
print(list7)
max4 = list7[0]
min4 = list7[0]
for i in list7:
	if i > max4:
		max4 = i
print(max4)
for j in list7:
	if j < min4:
		min4 = j
print(min4)
list7[7] = list7[0]           # 赋值先后顺序!
list7[3] = list7[-1]
list7[0] = max4
list7[-1] = min4
print(list7)

max = max(list)
max_index = list1.index(max)
list1[0],list1[max_index] = list1[max_index],list1[0]    # 交换!!



# 5.在控制台输入一句英语，获得每个字母出现的次数，注：每个字符作为key,出现的次数作为value生成一个字典
English_world = input("请输入一句英语:")
dict_num = {}
for item in English_world:           # item是每个字符
	# if item not in dict_num:       # not in dict_num.keys(),不用考虑in不in!
		dict_num[item] = English_world.count(item)
print (dict_num)

