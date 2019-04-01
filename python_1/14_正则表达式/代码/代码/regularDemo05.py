import  re

#子模式
#()
#如果在正则表达式中出现\1  \2等标识符的时候，那么\1代表从左向右的第一个（）中的内容。。。被称为子模式【简化正则表达式】
pattern = re.compile(r"<([a-z]+)><(\w+)>\w+</\2></\1>")
ret = pattern.search("<div><span>hello</span></div>")
print(ret.group())
#子模式访问
print(ret.group(1))
print(ret.group(2))
