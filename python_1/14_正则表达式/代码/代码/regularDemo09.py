import  re

#注意问题
#1.match，findall，search之间的区别
a = re.search(r"[\d]","abc3ab5").group()
print(a)   #3

b = re.findall(r"[\d]","abc3ab5")
print(b)  #['3']

c = re.match(r"[\d]","abc3")
print(c)  #None

#2.flags的用法【模式修正】
print(re.split("a","1A2a3A4a",re.I))   #['1A2', '3A4', '']
"""
split(pattern,string,maxsplit,flags),当传入三个参数的时候，表示只匹配前三个参数，flags不起作用
"""
#解决方案：关键字参数
print(re.split("a","1A2a3A4a",flags=re.I))

#3.使用split函数之后去除""
poem = "床前明月光,疑是地上霜.举头望明月，低头思故乡。"
list1 = re.split(r"[,.，。]",poem)
print(list1)  #

for item in list1:
    if item == "":
        list1.remove("")

print(list1)  #['床前明月光', '疑是地上霜', '举头望明月', '低头思故乡']




