# 集合set:只有key,没有value的一个字典

# 根据这个原理可以得到:
# 1.字典中的key不允许重复,所以set中不会出现重复元素
# 2.字典中的key只能是不可变对象,所以set中也只能放置不可变对象

# 第一种创建几个的方式
set1 = {1,2,3,4,5}
print(set1)
print(type(set1))
# 第二种创建方式,借用列表list,元组,字符串,字典
list1 = ["a","b","c","d"]
set3 = set(list1)
print(set3)

tuple1 = (1,1,2,3,4,5)
set4 = set(tuple1)
print(set4)

string = "hello"     # 会拆开字符串,并去重,乱序
set5 = set(string)
print(set5)

dict1 = {"name":"xiaoming","age":29,"money":1000}
set6 = set(dict1)               # 只会获取键组成集合
print(set6)

set7 = set()        # 空集合
dict8 = {}           # 空字典,不是空集合

# 添加元素
set7.add(1)         # 如果元素已经存在,会自动去重
print(set7)         # 因为集合中都是key,不允许使用可变对象.

# 可变对象:list,dic
# 不可变对象:tuple,number,string

# .update()  将括号内的参数进行for循环遍历,然后将每个元素加入集合中
# 参数不能是数字,因为数字无法遍历
set8 = set()
set8.update([1,2,3,4])
set8.update((1,2,3,4,"hello"))     # 去重
set8.update({"name":"xiaoming","age":29})
print(set8)

# 查找 遍历查询 for in
for item in set8:
	print(item)

# for index,item in enumerate(set8):    # index只是位置编号,不能作为索引

# 删除 remove（）删除指定元素
set8.remove("name")     # 删除不存在的元素会crash
print(set8)

set8.discard(9)       # 使用discard删除元素时,不存在也不会崩溃

# 没有修改说法,集合不支持下标