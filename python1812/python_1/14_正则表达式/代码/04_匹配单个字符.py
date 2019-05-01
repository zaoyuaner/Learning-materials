import re

# .  匹配任意单个字符,除了换行符
# b在前  k在后, 中间任意单个字符
# 匹配的: bok  bak  bck  bbk  bkk  b@k  b*k等
# 不匹配: bk  b\nk
result = re.match(r"b.k","b*k")
print(result)           # <re.Match object; span=(0, 3), match='b*k'>


# [abc]    这一位可以是a 或 b 或 c
# 匹配:  bak bbk bck
# 不匹配: bnk  bdk b k  b*k
result = re.match(r"b[abc]k","bck")
print(result)           # <re.Match object; span=(0, 3), match='bck'>

# [0123456789]  限制这一位只能是数字
# [a-z]   限制这一位只能取小写字母
# [A-Z]   限制这一位只能取大写字母
# [0-9]   限制这一位只能是数字
# [0-9a-zA-Z] 限制这一位支持字母,数字
# [0-9a-zA-Z_] 支持字母,数字,下划线

# [^abc]   限制这一位不能是a或b或c   脱字符
# [^0-9]   这一位必须非数字
# [^a-zA-Z]  这一位必须非字母
result = re.match(r"b[^abc]k","bck")
print(result)           # None

# 转义字符
# \d  ==> [0-9]      是数字
# \D  ==> [^0-9]     不是数字
# \w  ==> [0-9a-zA-Z_]  匹配数字,字母,下划线
# \W  ==> [^0-9a-zA-Z]  是特殊字符
# \s  ==> 匹配不可见字符(空格,换行),一个
# \S  ==> 匹配可见字符 , 一个

# 生成正则表达式对象   一般不用这种方法
pattern = re.compile(r"\d[a-z_]")   # 数字+小写字母的两位字符
# 通过正则表达式对象来匹配
result = pattern.match("2_6666")   # 结尾被忽略了!从开头开始匹配
print(result)
# print(result.group())    # group就是匹配到的字符串