from threading import Thread, Condition
import time

condition = Condition()


def odd():
    for i in range(1, 10, 2):
        with condition:
            print(i)
            time.sleep(1)
            condition.notify()
            # 通知其他线程
            condition.wait()


def even():
    for i in range(0, 10, 2):
        # 获取condition的锁
        with condition:
            print(i)
            time.sleep(1)
            # 停下来
            condition.wait()
            # 通知其他线程
            condition.notify()


if __name__ == '__main__':
    Thread(target=even).start()
    Thread(target=odd).start()
