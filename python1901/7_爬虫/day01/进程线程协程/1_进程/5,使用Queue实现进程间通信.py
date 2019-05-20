from multiprocessing import Queue, Process
import time
import random
import queue


def write(q):
    print('写进程开始执行')
    while True:
        value = random.randint(0, 100)
        try:
            q.put(value, block=True, timeout=5)
            print(f'{value}已经被存入Queue中')
        except queue.Full:
            print('队列已满')
        # time.sleep(1)


def read(q):
    print('读进程开始执行')
    while True:
        try:
            value = q.get(block=False)
            print(f'{value}已被取出')
            time.sleep(2)
        except queue.Empty:
            print('队列为空')


if __name__ == '__main__':
    print('主进程开始执行')
    q = Queue(5)

    # 创建写进程
    # for i in range(5):
    #     p_write = Process(target=write, args=(q, ))
    #     p_write.start()

    # time.sleep(2)
    # # 创建读进程
    #
    for i in range(2):
        p_read = Process(target=read, args=(q,))
        p_read.start()

    # p_write.join()
    # p_read.join()
    print('主进程结束')
