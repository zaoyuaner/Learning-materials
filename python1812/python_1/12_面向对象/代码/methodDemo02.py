class SuperClass(object):
    @staticmethod
    def show():
        print("父类中的静态方法")

    @classmethod
    def check(cls):
        print("父类中的类方法")

class SubClass(SuperClass):
    pass

s = SubClass()
s.show()
s.check()
