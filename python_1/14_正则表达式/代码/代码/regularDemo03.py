import  re
"""
-------------------匹配多个字符------------------------

说明：下方的x、y、z均为假设的普通字符,n、m（非负整数），不是正则表达式的元字符
(xyz)    匹配小括号内的xyz(作为一个整体去匹配)
x?       匹配0个或者1个x
x*       匹配0个或者任意多个x（.* 表示匹配0个或者任意多个字符(换行符除外)）
x+       匹配至少一个x
x{n}     匹配确定的n个x（n是一个非负整数）
x{n,}    匹配至少n个x
x{n,m}   匹配至少n个最多m个x。注意：n <= m
x|y      |表示或，匹配的是x或y
"""

#（）当做一个整体去匹配，返回的结果为一个列表
print(re.findall(r"(ab)","aaacccaabbbbb"))

print(re.findall(r"a?","aaacccaabbbbb"))

print(re.findall(r"a*","aaacccaabbbbb"))

print(re.findall(r"a+","aaacccaabbbbb"))
"""
['a', 'a', 'a', '', '', '', 'a', 'a', '', '', '', '', '', '']
['aaa', '', '', '', 'aa', '', '', '', '', '', '']
['aaa', 'aa']
"""
#恰好出现n次
print(re.findall(r"a{2}","aaacccaabbbbb"))

#至少出现n次
print(re.findall(r"a{2,}","aaacccaabbbbb"))

#{m,n}：至少出现m次，至多出现n次
print(re.findall(r"a{2,5}","aaacccaabbbbb"))

#表示或
print(re.findall(r"a|b","aaacccaabbbbb"))   #[ab]