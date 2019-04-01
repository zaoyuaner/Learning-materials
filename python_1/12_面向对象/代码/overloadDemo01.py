print(1 + 1)
print("1" + "1")
#print("1" + 1)
#不同的数据类型进行加法运算得到的是不同的解释

#思考问题：两个对象相加？
class Person(object):
    def __init__(self,num):
        self.num = num

    def __str__(self):
        return "num=" + str(self.num)

    def __add__(self, other):
        #两个对象相加得到的结果仍然为一个对象
        return Person(self.num + other.num)   #Peson(30)


p1 = Person(10)
p2 = Person(20)

print(p1)  #10
print(p2)  #20

print(p1 + p2)  #30

#p1 + p2----->p1.__add__(p2),