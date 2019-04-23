## 文件读写操作
1. 有一个jsonline格式的文件file.txt大小约为10K(读取文件)
```
def get_lines():
    with open('file.txt', 'rb') as f:
	return f.readlines()

if __name__ == '__main__':
    for e in get_lines():
	process(e) # 处理每一行数据
```

2. 现在要处理一个大小为10G的文件，但是内存只有4G，如果在只修改get_lines 函数而其他代码保持不变的情况下，应该如何实现？需要考虑的问题都有那些？
```
def get_lines():
    with open('file.txt','rb') as f:
        for i in f:
            yield i


from mmap import mmap


def get_lines(fp):
    with open(fp,"r+") as f:
        m = mmap(f.fileno(), 0)
        tmp = 0
        for i, char in enumerate(m):
            if char==b"\n":
                yield m[tmp:i+1].decode()
                tmp = i+1

if __name__=="__main__":
    for i in get_lines("fp_some_huge_file"):
        print(i)

```
> 要考虑的问题有：内存只有4G无法一次性读入10G文件，需要分批读入分批读入数据要记录每次读入数据的位置。分批每次读取数据的大小，太小会在读取操作花费过多时间。

3、补充缺失的代码
```
def print_directory_contents(sPath):
"""
这个函数接收文件夹的名称作为输入参数
返回该文件夹中文件的路径
以及其包含文件夹中文件的路径
"""
import os
for s_child in os.listdir(s_path):
    s_child_path = os.path.join(s_path, s_child)
    if os.path.isdir(s_child_path):
        print_directory_contents(s_child_path)
    else:
        print(s_child_path)

```

## 模块与包
4、控制台输入日期，判断这一天是这一年的第几天？
```
import datetime
def dayofyear():
    year = int(input("请输入年份："))
    month = int(input("请输入月份："))
    day = int(input("请输入天："))
    date1 = datetime.date(year=year,month=month,day=day)
    date2 = datetime.date(year=year,month=1,day=1)   #定义起始日期
    return (date1-date2).days + 1
```

5、打乱有序list？
```
import random
alist = [1,2,3,4,5]
random.shuffle(alist)#调用shuffle()方法
print(alist)
```

## 数据类型
6、给现有字典按value值排序？
```
d= {'a':24,'g':52,'i':12,'k':33}

sorted(d.items(),key=lambda x:x[1])
```
7、字典推导式
```
d = {key:value for (key:value} in iterable}
```
8、反转字符串
```
print("aStr"[::-1])  #反向切片
```
9、将字符串 "k:1 |k1:2|k2:3|k3:4"，处理成字典 {k:1,k1:2,...}   split()方法
```
def str_dict(str1):
    dict1 = {}
    for items in str1.split('|')：
        key,value = items.split(':')
        dict1[key] = value
    return dict1

str1 = "k:1|k1:2|k2:3|k3:4"
str_dict(str1)
```
10、请按alist中元素的age由大到小排序(sorted()函数结合匿名函数的用法)
```
def sort_by_age(alist):
    return sorted(alist,key=lambda x:x['age'],reverse=True)

alist = [{'name':'a','age':20},{'name':'b','age':30},{'name':'c','age':25}]
sort_by_age(alist)
```
11、list = ['a','b','c','d','e']  print(list[10:])  代码的输出结果将是什么？
```
代码将输出[],不会产生IndexError错误，就像所期望的那样，尝试用超出成员的个数的index来获取某个列表的成员。例如，尝试获取list[10]和之后的成员，会导致IndexError。然而，尝试获取列表的切片，开始的index超过了成员个数不会产生IndexError，而是仅仅返回一个空列表。这成为特别让人恶心的疑难杂症，因为运行的时候没有错误产生，导致Bug很难被追踪到。
```




























