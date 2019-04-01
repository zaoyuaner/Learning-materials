
# 封装一个函数,传入一个数,如果是质数返回True,合数返回False
def fn(num):
	for i in range(2,num):
		if num%i == 0:
			return False
	return True

print(fn(5))

num = 123
dic = {"age":12}
def change(num,dic):

	num -= 1
	dic["age"] -=1

change(num,dic)

print(num,dic["age"])
