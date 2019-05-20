from threading import Thread, Semaphore, current_thread, BoundedSemaphore
import time


# sema = Semaphore(3)
sema = BoundedSemaphore(3)

def run():
    sema.acquire()
    print('子线程开始执行', current_thread().name)
    time.sleep(3)
    print('子线程结束')
    sema.release()
    sema.release()


if __name__ == '__main__':
    print('主线程开始执行')
    for i in range(5):
        Thread(target=run).start()
