import re


# 正则表达式中 \d, . , \w , \s ,空格 ,这些都代表单个字符
# 如果要控制出现的次数,需要用到次数控制
result = re.match(r"\d\d\d\d","12341")


#  ?    前面表达式出现0^1次
result1 = re.match(r"bo?k","bk")    # 前面o出现0次或1次  b在前 k在后 ,o在中间出现0或者1次
print(result1)        # <re.Match object; span=(0, 3), match='bok'> o出现1次
				# <re.Match object; span=(0, 2), match='bk'> o出现0次

result2 = re.match(r"(bo)?k","bk")   # bo作为整体出现o次或者1次

#  *    前面表达式出现任意次  0`无穷大
result3 = re.match(r"bo*k","boooooooxoook")   # b在前k在后,o出现任意次
print(result3)                    # None  中间出现了x

result4 = re.match(r"(bo)*k","bobobok")   # k在后,bo出现任意次
print(result4)

# .*  任意字符任意次数
# \d*  任意数字任意次数

#  +    前面表达式出现1次以上  1^无穷大
result5 = re.match(r"bo+k","boook")   # b在前k在后,o出现1次以上,不能是bk
print(result)             # 也能用()分组

# { x,y }  至少出现x次 最多出现y次  x^y次
# { ,y }   出现 0^ y 次   x = 0
# { x, }   出现 x^ 无穷大 次  y = 无穷
# { x }    只能出现 x 次

result = re.match(r"bo{2,5}k","booooook")     # 超过5个
print(result)              # None

result = re.match(r"bo{,5}k","bk")
print(result)              # <re.Match object; span=(0, 2), match='bk'>

result = re.match(r"bo{2,}k","booooook")
print(result)

result = re.match(r"bo{2}k","booooook")
print(result)              # None

# x|y   匹配左边的表达式 或右边的表达式
result = re.match(r"\d{3,}|[a-z]{3,}","abc")    # 字母三次以上或者数字三次以上
print(result)

# 匹配15位身份证或18位身份证,最后一位可以使用X
result = re.match(r"^(\d{14}|\d{17})(\d|X)$","42092319941007X")
print(result)