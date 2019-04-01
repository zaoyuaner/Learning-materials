import re

#re模块中常用的函数

#1.compile()
str1 = "today is a good day"
str2 = r"\w*"
pattern1 = re.compile(str2)
print(pattern1.findall(str1))

#2.match()
result = re.match(r"[1-9]\d{4,10}","6725675786574657")
print(result)

#3.search()
#注意：只要匹配到一个符合条件的子字符串，则直接返回，后面的内容不参与搜索
print(re.search(r"\dcom","www.4comnghughs").group())

#4.findall()
#注意;返回的结果为列表
#finditer(): 返回的结果为可迭代器
iter = re.finditer(r"\d+","12 fjhaehgj 66 fhaj  ")
print(iter)

for i in iter:
    print(i)

    #获取值
    print(i.group())
    #获取下标
    print(i.span())


#5.split() :返回一个列表
s1 = "1one2two3445545three454four56977878five"
print(re.split(r"\d+",s1))
print(re.split(r"[0-9]{1,}",s1))
print(re.split(r"[^a-z]+",s1))

s2 = "zhangsan lilei      lisi    Han   Jack"
print(re.split(r" +",s2))

s3 = "zhangsan@@@@lilei##########lisi%%%Han&&&&&&&&&&&&&Jack"
print(re.split(r"[^a-zA-Z]+",s3))

#6.sub() 替换，返回的是替换之后的字符串
string1 = "today is a good day today is a good da"
#用-将空格替换
#参数：旧的字符换【正则表达式】  新的字符串   原字符串
print(re.sub(r"\s","-",string1))

#subn()  替换，返回一个元组（新的字符串，替换的次数）
print(re.subn(r"\s","-",string1))





