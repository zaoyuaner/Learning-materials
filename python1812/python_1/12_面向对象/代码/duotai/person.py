class Person(object):
    """
    def feedCat(self,cat):
        print("喂猫:",cat.name)
        cat.eat()
    def feedDog(self,dog):
        print("喂猫:",dog.name)
        dog.eat()
    """
    #多态
    #ani被当做父类的引用 ，当传参的时候，实参是一个子类对象的时候，则体现出了 多态的应用
    def feedAnimal(self,ani):   #ani = c   c = Cat("")
        print("喂动物:", ani.name)
        ani.eat()