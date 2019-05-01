
# 一般写入方法
fp = open("02.txt","w",encoding="utf-8")  # 换行符需要手动添加

fp.write("哈哈\n")
fp.write("welcome to beijing -- 毒死你个王八犊子\n")  # 请查看02.txt

fp.writelines(["111\n","222\n","333\n"])    # 写多行, 列表元素是字符串

fp.close()

# with写入
with open("03.txt","w",encoding="utf-8") as fp:
	fp.write("Whatever is worth doing is worth doing well该行很骄傲很关键")

