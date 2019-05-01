#单例类：将装饰器作用于一个类上
def singleton(cls):
    #类属性
    instance = {}

    #成员方法
    def getSingleton(*args, **kwargs):
        #思路：如果cls在字典中，则直接返回；如果不存在，则cls作为key，对象作为value，添加到字典中
        if cls not in instance:
            instance[cls] = cls(*args, **kwargs)
        return  instance[cls]

    return getSingleton

@singleton
class Test(object):
    pass

t1 = Test()
t2 = Test()

print(id(t1) == id(t2))
print(t1 is t2)



