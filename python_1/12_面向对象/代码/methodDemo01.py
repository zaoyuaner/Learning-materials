class Test(object):
    #1.类属性
    age = 100

    def __init__(self,name):
        #2.实例属性
        self.name = name

    #3.成员方法,通过对象调用
    #必须有一个参数，这个参数一般情况下为self，self代表是当前对象
    def func(self):
        print("func")

    #4.类方法
    """
    a.必须有一个参数，这个参数一般情况下为cls，cls代表的是当前类
    b.类方法是属于整个类的，并不是属于某个具体的对象，在类方法中禁止出现self
    c.在类方法的内部，可以直接通过cls调用当前类中的属性和方法
    d.在类方法的内部，可以通过cls创建对象
    """
    @classmethod
    def test(cls):
        print("类方法")
        print(cls)   #<class 'methodDemo01.Test'>
        print(cls.age)

        #6
        #注意：cls完全当做当前类使用
        c = cls("hello")
        c.func()

    #7.静态方法
    @staticmethod
    def show():
        print("静态方法")

t = Test("hjfsh")
t.func()

#5,.调用类方法
Test.test()   #类名.类方法的名称()
t.test()       #对象.类方法的名称()

#7。调用静态方法
Test.show()
t.show()
