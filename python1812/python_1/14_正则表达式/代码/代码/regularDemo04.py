import  re

#匹配分组
#|   :或
#()   :整体
#search:会在字符串中从左向左进行查找，如果找到第一个符合条件的，则停止查找
#正则1|正则2：只要正则1或者正则2中的一个满足，则直接按照这个条件查找
pattern = re.compile("\d+|[a-z]+")
ret = pattern.search("123-d223344aa$$aa")   #abc123-d223344aa$$aa
print(ret.group())

pattern = re.compile("([a-z]\d)+\w+")
ret = pattern.search("abc123-d223344aa$$aa")   #abc123-d223344aa$$aa
print(ret.group())


