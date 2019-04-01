import  re
"""
--------------锚字符(边界字符)-------------

^     行首匹配，和在[]里的^不是一个意思   startswith
$     行尾匹配                          endswith

\A    匹配字符串开始，它和^的区别是,\A只匹配整个字符串的开头，即使在re.M模式下也不会匹配它行的行首
\Z    匹配字符串结束，它和$的区别是,\Z只匹配整个字符串的结束，即使在re.M模式下也不会匹配它行的行尾

\b    匹配一个单词的边界，也就是值单词和空格间的位置   bounds
\B    匹配非单词边界

"""
#search()
print(re.search(r"^to","today is a good day"))
print(re.search(r"day$","today is a good day"))

#findall()
#re.M
print(re.findall(r"\Ato","today is a good day\ntoday is a good day",re.M))
print(re.findall(r"^to","today is a good day\ntoday is a good day",re.M))
#总结：\A只匹配第一行的行首，^匹配每一行的行首

#\b匹配边界【开始和结尾】，\B匹配的是非边界【中间】
print(re.search(r"er\b","never"))   #er
print(re.search(r"er\b","nerve"))   #None
print(re.search(r"er\B","never"))    #None
print(re.search(r"er\B","nerve"))   #er