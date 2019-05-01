# 子模式
# 每次使用() 对正则表达式进行分组时,系统会自动为分组打上编号. 由\1 ^\9 最多支持9个组

import re
result = re.match(r"(abc)(123)\1\2","abc123abc123")
# 此时 \1 = abc  \2 = 123   如果后面再接\2\1  !  就重复abc123了

print( result)
print( result.group(1))      # 第一个分组就是abc
print( result.group(2))      # 第二个分组就是123


# 此时\1 = 666  !=\d+  这个\1 不等于正则表达式,而是等于正则表达式所匹配的字符
# \2 = bbb  != [a-z]+
result = re.match(r"(\d+)([a-z]+)\1\2","666bbb666bbb")
print(result)                # None  \1 != 222   \2 != ttt
print( result.group(2))

# 提取区号
# 命名分组  (?P<名称>规则 )
res = re.match(r"(?P<aa>\d{3,4})-(?P<bb>\d{8})$","0755-12345678")
print(res.group(1),res.group("aa"))      # 提取命名分组
print(res.group()[2])                    # 5