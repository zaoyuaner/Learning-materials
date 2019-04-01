import  re
"""
----------匹配单个字符与数字---------
.                匹配除换行符以外的任意字符
[0123456789]     []是字符集合，表示匹配方括号中所包含的任意一个字符
[good]           匹配good中任意一个字符
[a-z]            匹配任意小写字母
[A-Z]            匹配任意大写字母
[0-9]            匹配任意数字，类似[0123456789]
[0-9a-zA-Z]      匹配任意的数字和字母
[0-9a-zA-Z_]     匹配任意的数字、字母和下划线
[^good]          匹配除了good这几个字母以外的所有字符，中括号里的^称为脱字符，表示不匹配集合中的字符
[^0-9]           匹配所有的非数字字符
\d               匹配数字，效果同[0-9]
\D               匹配非数字字符，效果同[^0-9]
\w               匹配数字，字母和下划线,效果同[0-9a-zA-Z_]
\W               匹配非数字，字母和下划线，效果同[^0-9a-zA-Z_]
\s               匹配任意的空白符(空格，回车，换行，制表，换页)，效果同[ \r\n\t\f]
\S               匹配任意的非空白符，效果同[^ \f\n\r\t]
"""
#[]  :只匹配其中的一位
# - ：表示一个区间
#1.
#1.1编译正则表达式返回对象
pattern = re.compile(r"[abcd]")   #正则表达式  [a-d]
#1.2使用正则表达式匹配字符串，成功返回对象，并携带匹配之后额结果，如果匹配失败则返回None
ret = pattern.match("dhello")    #需要被匹配的字符串
print(ret)
print(ret.group())

#2.
pattern = re.compile(r"[s-z]")
ret = pattern.match("xhello")
print(ret)
print(ret.group())

#3
pattern = re.compile(r"[0-9]")
ret = pattern.match("5hello")
print(ret)
print(ret.group())

#4
pattern = re.compile(r"[0-9a-zA-Z]")
ret = pattern.match("8hello")
print(ret)
print(ret.group())

#5  ^:脱字符【】否定的含义
pattern = re.compile(r"[^0-9]")
ret = pattern.match("chello")
print(ret)
print(ret.group())

#6 \d:只匹配数字，等同于[0-9]
pattern = re.compile(r"\d")
ret = pattern.match("4")
print(ret)
print(ret.group())

#7.   \w
pattern = re.compile(r"\w")
ret = pattern.match("7")
print(ret)
print(ret.group())

#8   \s
pattern = re.compile(r"\s")
ret = pattern.match("\t")
print(ret)
print(ret.group())

#9.   .：匹配不到换行符【\n】
pattern = re.compile(r".")
ret = pattern.match("\r")
print(ret)
print(ret.group())













