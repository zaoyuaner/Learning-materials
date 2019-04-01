# re.match         # 从第0位开始匹配字符串,匹配完成立刻结束,会忽略. 相当于匹配开头
# re.search        # 搜索整个字符串进行匹配,                     相当于匹配包含
# re.findall       # 检索整个字符串进行匹配,返回一个列表
import re
result = re.match(r"\d[a-z]","......3d")
print(result)            # None   从第0位开始匹配,一旦失败立刻返回None

result = re.search(r"\d[a-z]",".....3d")   # 搜索匹配
print(result)            # <re.Match object; span=(5, 7), match='3d'>
print(result.group())       # 3d  .group就是匹配到的值

result = re.findall(r"\d[a-z]",".....3d4f5t6a9")  # 检索整个字符串,匹配到就会放到列表中
print(result)          # ['3d', '4f', '5t', '6a']

# 匹配行首 ^  这里不写在中括号里面  中括号里面就是脱字符
result = re.match(r"^\d","1qqqqqqqq")      # 匹配字符串一定以数字开头,是就结束
print(result)

# 匹配行尾 $  用match 也会从头开始!  所以这里用.search
result = re.search(r"hello$","6666hello")      # 匹配字符串以hello结尾
print(result)

# 匹配开头加结尾 ^ $  \d[][]只能是三位数,指定开头指定结尾,不能包含  3aa3aa报错
result = re.search(r"^\d[a-z][a-z]$","3aa")      # 匹配字符串以hello结尾
print(result)


# re.M 如果字符串中有换行符\n, 匹配多行
# 在re.M模式下,使用^ 匹配行首时,支持多行匹配!
result = re.findall(r"^\d","1aaaaaa\n2dddddd\n3ffffff",re.M)
print(result)            # ["1","2","3"]

# \A  将多行字符串视作一行,只会匹配这一行的行首
result = re.findall(r"\A\d","1aaaaaa\n2dddddd\n3ffffff",re.M)
print(result)            # ["1"]

# 匹配多行行尾
result = re.findall(r"\d$","1aaaaaa1\n2dddddd2\n3ffffff3",re.M)
print(result)            # ["1","2","3"]

# \Z  将多行字符串视作一行,只会匹配这一行的行尾
result = re.findall(r"\d\Z","1aaaaaa1\n2dddddd2\n3ffffff3",re.M)
print(result)            # ["3"]

# \b  匹配单词边界 never单词  与hello单词之间以空格作为边界区分
result = re.search(r"er\b","never hello")      # 单词一定要以er结尾
print(result)

result = re.search(r"\bh","never hello")       # 单词一定要以h开头
print(result)

# \B  匹配单词非边界
result = re.search(r"\Ber\B","nerve hello")    # 不能出现在开头结尾,只能出现在单词中间
print(result)         # <re.Match object; span=(1, 3), match='er'>