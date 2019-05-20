from threading import Barrier, Thread, current_thread
import time


barrier = Barrier(3)

def run():
    barrier.wait()
    print('子线程开始执行', current_thread().name)
    time.sleep(3)
    print('子线程结束')


if __name__ == '__main__':
    print('主线程开始执行')
    for i in range(2):
        Thread(target=run).start()

    time.sleep(2)
    Thread(target=run).start()
    print('主线程结束')
