import re

# 数量/出现次数

# * : 表示前面字符出现的次数是任意多次，0~n
# + ：表示前面字符出现的次数是1次或多次
# ? : 表示前面字符出现0次或1次
# {} ： 次数范围
#   {4} : 4次
#   {4,} :至少4次
#   {,5} :最多5次
#   {4,10} : 4~10次
print(re.search('goo*gle', 'goooooogle'))
print(re.search('goo+gle', 'google'))
print(re.search('goo?gle', 'gooooogle'))
print(re.search('goog{4}le', 'googgggle'))
print(re.search('goog{4,}le', 'googgggggle'))
print(re.search('goog{4,6}le', 'googgggle'))
print(re.search('goog{,6}le', 'goole'))

# 贪婪模式 ： *  +  {}
# 非贪婪模式 : ?
# print(re.findall('g?', 'gggoogle'))  # ['g', 'g', 'g', '', '', 'g', '', '', '']
# print(re.findall('g*', 'gggoogle'))  # ['ggg', '', '', 'g', '', '', '']
# print(re.findall('g+', 'gggoogle'))  # ['ggg', 'g']
# print(re.findall('g{2,}', 'gggooggle'))  # ['ggg', 'gg']

print(re.findall('(go+)', 'gogoglegooglegkooglegoogle'))























