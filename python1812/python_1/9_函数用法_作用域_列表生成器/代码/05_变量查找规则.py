# 变量查找规则: L -> E -> G -> B


num = abs(-9)         # ④

num = 20              # ③

def outer():
	num =30           # ②
	def inner():
		num = 40      # ①
		print(num)    # 40
	return inner

fn = outer()
fn()