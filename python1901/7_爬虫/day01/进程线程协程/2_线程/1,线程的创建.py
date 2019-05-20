from threading import Thread, current_thread
import time


def run(i):
    print(f'第{i}个线程开始执行', current_thread().name)
    time.sleep(10)
    print(f'第{i}个线程结束')


if __name__ == '__main__':
    print('主线程开始执行')
    for i in range(4):
        Thread(target=run, args=(i,), name=i+1).start()

    print('主线程结束')
