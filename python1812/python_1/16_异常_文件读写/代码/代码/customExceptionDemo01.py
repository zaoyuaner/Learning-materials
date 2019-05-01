class MyException(Exception):
    def __init__(self,msg):
        super(MyException,self).__init__()
        self.msg = msg

    def __str__(self):
        return self.msg

    def handle(self):
        print("出现了异常")

try:
     raise MyException("自己的异常的类型")
except MyException as e:
     print(e)
     e.handle()