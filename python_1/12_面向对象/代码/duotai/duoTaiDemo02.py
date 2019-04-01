from duotai.person import Person
from duotai.cat import Cat
from duotai.dog import Dog

#1.创建一个Person的对象
p = Person()

#2.创建一个Cat的对象
c = Cat("小白")

#3.人执行自己的行为
p.feedAnimal(c)

d = Dog("旺财")
p.feedAnimal(d)
