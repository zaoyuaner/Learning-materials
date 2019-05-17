''''''
import re


# 单个字符
# .  : 表示任意单个字符，除了换行
# print(re.sj,j,'go\ngle', re.S))  # re.S可以让.匹配到换行\n

# [] : 单个字符的范围
# [abc] : 匹配a或者b或者c
# [a-z] : 匹配a到z范围之间的单个字符
# [a-zA-Z0-9] : 匹配字母和数字
# [a-zA-Z0-9_] : 匹配字母数字下划线
# print(re.search('go[abc]gle', 'gocgle'))
# print(re.search('go[a-z]gle', 'go8gle'))
# print(re.search('go[a-zA-Z0-9_]gle', 'go9gle'))

# \d : 表示数字，相当于[0-9]
# \D : 表示非数字，相当于[^0-9]
# \w : 表示数字字母下划线，相当于[a-zA-Z0-9_]
# \W : 表示非数字字母下划线，相当于[^a-zA-Z0-9_]
# \s : 表示空格、换行\n、制表符\t、回车符\r、换页符\f
# \S : 表示非\s
# print(re.search('go\dgle', 'go9gle'))
# print(re.search('go\Dgle', 'go,gle'))
# print(re.search('go\wgle', 'go_gle'))
# print(re.search('go\Wgle', 'go,gle'))
# print(re.search('go\s\sgle', 'go \ngle'))


# 边界字符
# ^ : 开头匹配
# $ ：结尾匹配
# ^pattern$ ： 完全匹配, 必需和指定正则内容一致，不能有多余的内容
# print(re.search('^google', 'google123'))
# print(re.search('google$', 'google123google'))
# print(re.search('^google$', 'google123google'))  # None
# print(re.search('^goo.*gle$', 'google123google'))

# 表示数量
# * ： 表示前面字符出现任意多次：0~n

# \A : 跟 ^类似
# \Z : 跟 $类似
# \Apattern\Z : 完全匹配
# 区别：换行模式下，每一行都会重新进行正则匹配
# print(re.findall('\A#', '#baidu\n#google\n#360', re.M))  # ['#']
# print(re.findall('^#', '#baidu\n#google\n#360', re.M))  # ['#', '#', '#']

# 单词边界
# \b ：单词是否以某个字符串结尾
# \B ：单词是否不以某个字符串结尾
print(re.search(r'google\b', 'google123 123google abcgoogle'))
print(re.search(r'google\B', 'google123 123google abcgoogle'))


# 重要字符
#  . [] \d \w \s
#  ^ $  ^$



















