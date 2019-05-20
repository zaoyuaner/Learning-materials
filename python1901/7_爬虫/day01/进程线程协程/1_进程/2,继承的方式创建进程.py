from multiprocessing import Process
import time


class MyProcess(Process):
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
    myprocess = MyProcess('hot and moist')

    # 设置为守护进程
    myprocess.daemon = True
    myprocess.start()
    print(myprocess.pid)
    print(myprocess.is_alive())
    myprocess.terminate()
    myprocess.join()

    n = 0
    while n <= 5:
        print('good day')
        time.sleep(1)
        n += 1
    print(myprocess.is_alive())
