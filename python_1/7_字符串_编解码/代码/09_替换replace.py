# 替换
# .replace(old,new,maxCount)  使用new替换old,可以指定替换次数

str1 = "this is a test test test"
print(str1.replace("test","school"))  # 不带次数则替换所有
print(str1.replace("test","exam",2))

# .maketrans()   translate 翻译.  可以使用映射表进行简单加密
# str.maketrans()    # 创建一个翻译表,字符映射表
table = str.maketrans("hlo","abc")   # hlo翻译成了ASCII码,对应123
print(table)     # {104: 49, 108: 50, 111: 51}  输出为字典

# .translate()  翻译
str2 = "hello"
str3 = str2.translate(table)    # 使用table映射表翻译str2
print(str3)

