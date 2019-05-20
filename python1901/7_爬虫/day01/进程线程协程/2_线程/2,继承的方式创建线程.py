from threading import Thread
import time


class MyThread(Thread):
    def __init__(self, desc, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.desc = desc

    def run(self):
        while True:
            print(f'{self.desc} day')
            time.sleep(1.2)

    def func(self):
        pass


if __name__ == '__main__':
    myThread = MyThread('hot and moist')

    # 设置为守护进程
    myThread.daemon = True
    myThread.start()
    # print(myThread.pid)
    print(myThread.is_alive())
    # myThread.terminate()
    # myThread.join()

    n = 0
    while n <= 5:
        print('good day')
        time.sleep(1)
        n += 1
    print(myThread.is_alive())
