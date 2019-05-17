# 对于不可变对象:数字,字符串,元组   进行传参,传递的都是值. 形参做任何修改都对实参无影响
# 传值
def exchange(num1,num2):
	num1,num2 = num2,num1
	print("在函数中:",num1,num2)

num1 = 10
num2 = 20
exchange(num1,num2)      # 允许实参和形参同名,没有任何影响
print("在函数外:",num1,num2)   # 传值,函数进行任何运算都和实参无关!


# 对于可变对象: 列表,字典,集合  进行传参,传递的都是引用. 形参改变,实参改变!
# 传引用
def change(list1):
	list1[0] = "a"
	print("函数内:",list1)

list0 = [1,2,3,4]
change(list0)               # list0 = list1 可变对象实际上
							# 是让list1和list0指向同一片内存空间
print("函数外:",list0)

# 字典的传引用
def change2(dict1):
	dict1["name"] = "zhangsan"
dict1 = {"name":"xiaoming"}
change2(dict1)
print(dict1)