import re

#贪婪和非贪婪【匹配一位还是匹配多位的区别】
#+   *  ：多次匹配【贪婪匹配】
#在+或者*后面添加？则改为非贪婪匹配
result1 = re.findall(r"a(\d+)","a23333333b")
print(result1)   #['23333333']

result1 = re.findall(r"a(\d+?)","a23333333b")
print(result1)   #['2']

#特殊情况;如果一个正则表达式的前后都有限定条件的时候，那么则不存在贪婪模式，？将不起作用
result1 = re.findall(r"a(\d+)b","a23333333b")
print(result1)
result1 = re.findall(r"a(\d+?)b","a23333333b")
print(result1)


