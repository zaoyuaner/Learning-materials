# 匹配一位还是匹配多位的区别
import re
#  * ,+ ,{x,} ,{,y}

# 贪婪: 尽可能多的进行匹配,取最大匹配结果   * +  ?(取一次) 默认是贪婪模式
# 非贪婪: 尽可能少的进行匹配,取最小匹配结果  *?  +?  ??(取0次)非贪婪模式

result = re.match(r"a\d+","a1234567890")     # 贪婪模式
print(result)      # <re.Match object; span=(0, 11), match='a1234567890'>

result = re.match(r"a\d+?","a1234567890")    # 惰性模式
print(result)      # <re.Match object; span=(0, 2), match='a1'>

# 匹配?出现0到1次
result = re.match(r"\???","???")   # 使用\转义特殊字符 \.  \% \+  \* \? \\
print(result)          # 匹配0次  <re.Match object; span=(0, 0), match=''>