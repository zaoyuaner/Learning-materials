# 查找
# .find()   在字符串中寻找子串是否存在,如果存在返回下标(0以上的正数),不存在返回-1
str2 = "abcd efhello123hello"
print(str2.find("o"))       #find（str[,start,end]）默认返回第一次找到的元素下标
print(str2.find("2",10,1000))    # 指定区间,从第10个下标开始寻找
print(str2.find("hello"))    # 第一个hello 子串整体匹配

# .rfind()   从右到左  返回的下标依然从0开始计算
print(str2.rfind("hello"))   # 第二个hello
print(str2.rfind("2",10,1000))    # 指定区间

# .index()
# index和find一样,也是寻找子串位置,但是index找不到会崩溃,find找不到返回-1
print(str2.index("a"))

# .rindex()   从右往左
print(str2.rindex("o"))    # 19
print(len(str2))           # 20

# max()   min()    实际比较ASCII码
print(max(str2))
print(min(str2))     # 输出为空格!ASCII码为32,小于字母


