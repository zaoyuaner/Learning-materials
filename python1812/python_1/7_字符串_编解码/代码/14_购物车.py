# 简单的购物车

# 商品列表
goods_list = [
	("macBook",10000),
	("iPhone X",8000),
	("huawei",4000),
	("xiaomi",2000),
]
# 购物车
shopping_car = []
# 余额
money = input("请输入金钱:")

# 确保输入的金钱有效
if money.isdigit():
	# 将这个金钱转成数字
	money = int(money)

	# 购物操作可以进行多次所以使用while死循环,20000能买两个mac,所以需要重复显示mac
	# 使用循环的原因,根本不知道循环多少次,所以只能让客户自己break!
	while True:

		# 显示商品列表   枚举商品列表,下标,元组
		print("商品列表--------------------")
		for index,item in enumerate(goods_list):
			print(index,item)
		print("当前可用余额:",money)
		print("--------------------------")

		# 商品选择完了,需要用户选择了
		choice = input("请选择商品编号:,或输入q退出")

		# 如果是数字,则代表选择了商品编号
		if choice.isdigit():
			choice = int(choice)
			if 0 <= choice < len(goods_list):
				goods = goods_list[choice]      # 通过商品下标获取一个元组

				# 如果money大于等于goodsde价格,goods[1]为价格
				if money >= goods[1]:
					# 将商品放入购物车
					shopping_car.append(goods)
					# 将余额减去商品价格
					money -= goods[1]
				else:
					print("余额不足")
			else:
				print("输入商品编号错误")

		elif choice == "q":
			# 显示购物车的内容和余额
			for item in shopping_car:
				print(item)
			print("购物后还剩余额:",money)
			# 要退出循环使用break
			break
		else:
			print("输入有误!")

else:
	print("输入金钱错误!")
