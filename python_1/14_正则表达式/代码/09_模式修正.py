# re.I  ignore 忽略大小写

# re.M  multi 多行模式

# re.S  single 视作一行

import  re
# 忽略大小写匹配
result = re.findall(r"a","a1A2a3A4",re.I)
print(result)           # ['a', 'A', 'a', 'A']

# 多行匹配
result = re.findall(r"^\d","1aaaaa\n2bbbbb\n3ccccc",re.M)
print(result)           # ['1', '2', '3']