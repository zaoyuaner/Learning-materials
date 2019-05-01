# 功能,函数,方法,function

# 1.增加 append() 仅能追加一个元素
# 功能: 在列表尾部,追加一个元素
# 返回值: 没有返回值
# 是否修改原列表: 是
list1 = ["a","b","c","d","e","f"]
result = list1.append("g")
print(result)
print(list1)

# 追加一个子列表
list1.append(["1","2"])    # 可追加,结果为二维列表list.append(["1","2"])
print(list1)

# extend()  扩展,在列表的末尾添加元素
# 功能:在列表的末尾进行扩展,会将两个列表合并
# 返回值: None
# 能否修改原列表: 是
list1 = ["32","f","g","32","32"]
result = list1.extend(["1","3"])
print(result)
print(list1)

# insert()   插入元素
# 功能: 在列表的索引位置插入元素
# 返回值:  None
# 修改原列表: 是
result = list1.insert(0,"hello")    # (位置,对象)
print(result)
print(list1)

# pop 从列表弹出一个指定索引元素
# 功能: 从列表弹出一个元素,并且将这个元素从列表移除,默认弹出最后一个
# 返回值: 被弹出的元素
# 是否修改原列表: 是
result = list1.pop(-2)      # 括号中默认为-1
print(result)
print(list1)

del list1[3]    # 索引
print(list1)

# remove  从列表移除一个元素,从左到右移除找到的第一个
# 功能:
# 返回值: None
# 是否修改原列表:是
result = list1.remove("32")  # 移除指定的元素,只会移除一次.
print(result)
print(list1)

# 总结:使用索引移除,可以使用del,pop .
#      使用元素对比移除,使用remove.

# clear()  清空列表
result = list1.clear()
print(result)
print(list1)

# len()  返回列表的长度
list1 = [1,2,3,4,5,2,2,2,3]
print(len(list1))
print(len("helloworld"))

# max min 返回列表中的最大值最小值  .没有平均数函数avg
print(max(list1))
print(min(list1))

# index 返回指定函数的索引
print(list1.index(3))   # 返回3在list1中的索引.默认返回找到的第一个
print(list1.index(3,4,20))  # 在list1第4个到第20个索引中去查找3的索引

# count  统计元素在列表中出现的次数
print(list1.count(2))

# reverse()  倒序输出列表
result = list1.reverse()
print(result)
print(list1)

# sort() 对原列表进行排序,默认为升序,如果是字符串,比较ASCII码
result = list1.sort()
print(result)         # 无返回值
print(list1)

# 字符串比较规则,依次比较字符串的每一位,直至比较出大小为止.
list3 = ["hello","jsoo","masld","jhang"]
list3.sort()
print(list3)

# 降序排列
list3.sort(reverse=True)
print(list3)

# 使用绝对值排序
list5 = [1,2,-3,4,5,-2,2,2,3]
list5.sort( key=abs )         # key后面接用于排序的函数,abs 求绝对值
print(list5)

# 比较字符串的长度
list3 = ["hello","jsoo","m33124asld","jhang"]
list3.sort( key=len ,reverse= True )    # 让每个元素都来调用len函数获取长度,再排序
print(list3)

# sorted()   对列表排序,返回一个新列表,对原列表没有影响
list6 = [1,2,3,4,5,2,2,2,3]
list4 = sorted(list6 ,key= abs, reverse=True)
print(list4)

list = ["2","3","3",33,332,4]
print(len(list))

