
#
import _thread
import threading
import time


# 子线程的执行函数
def fn1(*args):
    print(args)
    print(threading.current_thread().name)  # 当前线程名


# 创建线程方式1
def create_thread1():
    # ’MainThread‘ 主线程名称
    # print(threading.current_thread().name)  # 当前线程名

    # 这种方式创建的默认是守护线程
    #   守护线程：子线程会随着主线程的结束而结束，
    #        子线程是忠臣，主线程是主公
    _thread.start_new_thread(fn1, ('BIGBANG', '胜利'))
    print('hello')

    time.sleep(10)  # 阻塞主线程，让主线程不停止


# 子线程2
def fn2(*args):
    print(args)
    print(threading.current_thread().name)


# 创建线程方式2
def create_thread2():
    t = threading.Thread(target=fn2, daemon=False, name='BIGBANG', args=('权志龙', '胜利'))
    t.start()  # 启动线程
    print('hello')


# 创建线程方式3
class MyThread(threading.Thread):
    def __init__(self, name, url):
        super().__init__()
        self.name = name
        self.url = url  # 自定义属性

    # 重写run，会自动调用，里面是子线程
    def run(self):
        # 子线程
        print('mythread:', threading.current_thread().name)


def create_thread3():
    t = MyThread('五月天', 'http://www.baidu.com')
    t.start()


if __name__ == '__main__':
    # create_thread1()
    # create_thread2()
    create_thread3()

    # print(threading.current_thread().name)  # 当前线程名





