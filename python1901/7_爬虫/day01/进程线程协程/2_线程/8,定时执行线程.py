from threading import Timer, current_thread
import time


def run():
    print('子线程开始执行', current_thread().name)
    time.sleep(3)
    print('子线程结束')


if __name__ == '__main__':
    print('主线程开始执行')
    t = Timer(5, run)
    t.start()

    print('主线程结束')
