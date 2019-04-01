class Animal(object):
    def __init__(self,arg):
        super(Animal, self).__init__()
        self.arg = arg


class Tiger(Animal):
    age = 100
    height = 200

    def __init__(self,name):
        #super(Tiger, self).__init__(name)
        self.name = name

    def haha(self):
        print("haha")

    @classmethod
    def test(cls):
        print("cls")

    @staticmethod
    def show():
        print("show")


if __name__ == "__main__":

    #1.__name__
    print(Tiger.__name__)  #Tiger

    t = Tiger("")
    #print(t.__name__)  #AttributeError: 'Tiger' object has no attribute '__name__'

    #2.__dict__
    print(Tiger.__dict__)  #类属性，所有的方法
    print(t.__dict__)   #实例属性

    #3.__bases__，获取指定类的所有的父类，返回的是一个元组
    print(Tiger.__bases__)