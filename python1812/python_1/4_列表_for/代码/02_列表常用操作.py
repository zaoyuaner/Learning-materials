# 1.合并列表,使用+
list1 = [1,2,3,4]
list2 = ["a","v","b","as"]
list3 = list1 + list2
print(list3)

# 2.重复列表  使用*
list4 = ["2a","asd","sdad"]
list5 = list4 *3
print(list5)

# 去重
set1 = set(list5)
list6 = list(set1)
print(list6)           # 瞎折腾,只能保证无重复,不能保证顺序

# 判断元素是否在列表中
print("a" in list2)
