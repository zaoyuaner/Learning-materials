
# 正则表达式  定义一个规则
import re
print(re.match("^[0-9]+$","123"))    # ^[0-9]  数字开头

# 前缀和后缀
str1 = "hello world"
print(str1.startswith("h"))      # True  判断是否已h开头,是返回真
print(str1.startswith("hello"))  # True
print(str1.startswith("w",6,100))  # True 选定区间判断是否已w开头

print(str1.endswith("d"))       # True  判断是否已d结尾,是返回真
print(str1.endswith("world"))
print(str1.endswith("o",0,5))   # True 选定区间,判断是否已o结尾



