class Singleton(object):
    #类属性
    instance = None

    #类方法
    @classmethod
    def __new__(cls, *args, **kwargs):
        #如果instance的值不为None，说明已经被实例化了，则直接返回；如果为NOne，则需要被实例化
        if not cls.instance:
            cls.instance = super(Singleton,cls).__new__(*args, **kwargs)

        return cls.instance

class MyClass(Singleton):
    pass

#当创建对象的时候自动被调用
one = MyClass()
two = MyClass()

print(id(one))
print(id(two))

print(one is two)


