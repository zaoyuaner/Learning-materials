#单例类
class Foo(object):
    #1.声明一个变量【类属性】
    instance = None

    #2.向外界提供一个公开的方法，用于返回当前类唯一的对象
    #方法命名格式：defaultInstance,currentInstance ,getInstance
    @classmethod
    def getInstance(cls):
        if cls.instance:
            return cls.instance
        else:
            #实例化
            cls.instance = cls()
            return  cls.instance

obj1 = Foo.getInstance()
obj2 = Foo.getInstance()

print(id(obj1) == id(obj2))
print(obj1 is obj2)


