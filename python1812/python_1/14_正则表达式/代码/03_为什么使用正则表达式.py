# 正则表达式: 使用简单的一些字符,能够匹配复杂的规则字符串

# 验证QQ号
# 1.6位以上,15以下
# 2.必须是全数字
# 3.不能以0开头    00000~99999

def checkQQ(str1):
	# 全数字
	if str1.isdigit():
		# 判断位数
		if 6 <= len(str1) <= 15:
			# 不能以0开头
			if str1[0] !=0:
				return True
			else:
				return False
		else:
			return False
	else:
		return False

print( checkQQ("1072368564"))

# 使用正则表达式,一句话搞定
import re

# r"[1-9][0-9]{5-14}"  第一位不能为0,[]代表第一位的取值范围,[0-9]后面数字0-9可以出现5-14次
result = re.match(r"[1-9][0-9]{5,14}","1072368564")       # 前面是规则, 后面是用来校验的字符串
print(result)

# re.match  匹配成功返回结果,匹配失败返回None