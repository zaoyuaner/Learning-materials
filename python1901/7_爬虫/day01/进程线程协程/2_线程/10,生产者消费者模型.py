import threading
import queue
import time
import random


condition = threading.Condition()


# 生产者
def producer(i, q):
    print(f'生产者子线程{i}开始执行')

    while True:
        with condition:
            value = random.randint(0,100)
            if not q.full():
                print(f'生产者子线程{i},生产了{value}')
                q.put(value)
                time.sleep(1)
            else:
                # 通知消费者消费
                print('队列已满,请消费')
                condition.wait()
                condition.notify_all()


# 消费者
def consumer(i, q):
    print(f'消费者子线程{i}开始执行')
    while True:
        with condition:
            if not q.empty():
                value = q.get()
                print(f'消费者子线程{i}, 消费了{value}')
                time.sleep(1)
            else:
                # 通知生产者生产
                print('队列已空,请生产.')
                condition.notify_all()
                condition.wait()


if __name__ == '__main__':
    print('主线程开始')
    q = queue.Queue(10)

    # 生产者线程
    for i in range(5):
        threading.Thread(target=producer, args=(i,q)).start()

    # 消费者线程
    for i in range(4):
        threading.Thread(target=consumer, args=(i, q)).start()

    print('主线程结束')
