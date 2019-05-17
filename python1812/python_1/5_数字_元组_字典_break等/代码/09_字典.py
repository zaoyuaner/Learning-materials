# # dic 无序哈希表,{key:value}
#
# # key唯一不可变,只能用不可变类型
# dic1 = {}         # 空字典
# dic2 = {"name":'小明',"age":20}     # 字典中存储的是键值对
# print(dic2)
#
# # 字典中的key只允许出现一次,后面会覆盖前面
# dict3 = {"name":"小明","age":20,"name":"我"}
# print(dict3)
#
# # 列表不可做键,因为列表可变.字符串数字元组可以作为key
# dict4 = {"name":"小明",10:100,(1,2,3):"good"}
#
# # 字典的访问,通过键来获取值
# dic5 = {"name":"xiaoming","age":20,"money":20}
# print(dic5["name"])       # 键不存在会crash
#
# # get 函数:如果该key存在会返回value值,若不存在会返回None
# result = dic5.get("name"，'hello')
# print(result)     没有的话可以直接赋值

#
# if result:
# 	print("存在这个键")
# else:
# 	print("不存在这个键")
#
# # 字典的添加和删除
# dict6 = {"name":"xiaoming"}
# dict6["sex"] = "男"         # dict[key] = value
# print(dict6)
#
# dict6["name"] = "zairian"   # 修改已存在的键值对,对于不存在的键则是添加
# print(dict6)
#
# # 删除: 1. del :直接删   2.pop :删除并返回
# dict7 = {"name":"xiaoping's","sex":"男"}
# result = dict7.pop("name")
# print(result)          # 删除这个键值对  返回值
# print(dict7)
#
# # del dict7["name"]
# print(dict7)
#
# # 遍历字典 只获取key
dict8 = {"name":"xiaoming","sex":"男","nash":"易"}
# for key in dict8:
# 	value = dict8[key]
# 	print(key,"=",value)
#
# # keys():获取所有键   values(): 返回所有值
# key_list = dict8.keys()
# for key in key_list:
# 	print(key)
#
# # items() 以列表的形式返回所有的键值对,每个键值对都是元组的形式
result = dict8.items()
print(result)
for key,value in result:
	print(key,"=",value)

for key,value in dict8.items():     # 同时返回键值对
	print(key,"=",value)

# 枚举法  i 为key在字典中的序号,无实际意义.
for i,key in enumerate(dict8):
	print(i,key)
	print(dict8[key])

# 键值交换  b = { v:k for k,v in a.items() } 去重

# 字典何必  a.update(b)
#
# # 示例
# # list1 = [0,1,2,3,4,5,6],list2 = ["Sun","Mon","Tue","Wed","Thu","Fri","Sat"].
# # 以list1中的元素作为key，
# # 以list2中的元组作为value生成一个新的字典dict2
# list1 = [0,1,2,3,4,5,6]
# list2 = ["Sun","Mon","Tue","Wed","Thu","Fri","Sat"]
# dict2 = {}
# if len(list1) == len(list2):
# 	for i in range(len(list1)):
# 		dict2[list1[i]] = list2[i]
# print(dict2)
#
