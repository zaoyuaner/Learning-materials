# 需求:移除列表中所有的23
list30 = [23,11,23,23,4,45,5556,23,113,23,42,323,23,23]

list30.remove(23)    # 只能移除一次
print(list30)

# remove 必须移除列表中存在的数,如果不存在就会崩溃.

# 先求出有多少个23,再来做移除
count = list30.count(23)
for i in range(count):       # 循环次数是0到count次
	list30.remove(23)
print(list30)

# 使用判断也可以(bug)
for item in list30:
	if item == 23:
		list30.remove(item)
print(list30)         # 删除前面这个23后,遍历的指针会自动后移,元素往前补位,所以会漏掉元素.
# 使用for in遍历列表式,最好不要做删除操作,导致元素会变位.
# [11, 4, 45, 5556, 113, 42, 323, 23, 23]

# # 删除元素后,遍历指针不往后移,让它-1原地踏步.
list1 = ["a","b","w","d","d","d","d","d","d","c","c","d"]
# for i in range(len(list)):
# 	if list[i] == "d":
# 		list1.remove("d")
# 		i -=1        # 删除"d"后列表长度变短,会越界.而且for循环中,删除列表元素无效.

# 如果想修改循环变量, 用while
i = 0
while i <len(list1):
	if list1[i] == "d":
		list1.remove("d")
		# i -=1       # 指针原地踏步, "d"删除干净
		continue       # 也可以使用continue 让后面的下标增加操作取消
	i +=1
print(list1)

# 总结: for i in range(len(list1):遍历开始时,就确定了列表长度,遍历过程不会发生变化.
#  while i<len(list1)  如果遍历时,list1中的元素,那么len(list1)就是实时变小.

