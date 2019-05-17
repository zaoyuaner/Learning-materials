#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author：zhangjiao
'''
将对象写入到磁盘
'''
import pickle


class Person():
    def __init__(self,name,age):
        self.name = name
        self.age = age


'''
序列化：将内存中的变量变成可读写或者是可传输的过程我们称之为序列化。
反序列化：将序列化的对象重新读到内存的过程，我们称之为反序列化。
'''

if __name__ == "__main__":
    per = Person("lili",18)
    per2 = Person("xiaoming",19)
    per3 = Person("xiaohua",20)

    #将对象进行序列化，序列化二进制的字符串。
    # res = pickle.dumps(per)
    # print(res)
    list1 = [per,per2,per3]
    with open("person.txt","wb") as f:
        f.write(pickle.dumps(list1))
        # f.write(pickle.dumps(per2))
        # f.write(pickle.dumps(per3))

    with open("person.txt","rb") as f2:
        #对对象进行反序列化处理
        list2 = pickle.loads(f2.read())
        # print(per2.name)
        # print(per2.age)
        print(list2[-1].name)

'''
将三个对象，同时存储到一个文件中，然后将这三个对象读出。
'''