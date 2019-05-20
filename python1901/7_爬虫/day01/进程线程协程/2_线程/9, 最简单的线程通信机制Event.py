from threading import Thread, Event
import time


event = Event()


def run():
    event.clear()
    print('子线程开始执行')
    event.wait()
    # time.sleep(2)
    print('子线程结束')


if __name__ == '__main__':
    print('主线程开始执行')
    Thread(target=run).start()
    time.sleep(2)
    event.set()

    Thread(target=run).start()
    print('主线程结束')


