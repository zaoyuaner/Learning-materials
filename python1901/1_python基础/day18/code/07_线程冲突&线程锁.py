import threading

# 线程冲突： 多个线程同时操作一个资源

# 全局变量
n = 0

# def fn():
#     global n
#     for _ in range(1000000):
#         n += 1
#     print(n)


# 线程冲突
# def thread1():
#     # 同时开启5个线程，同时去访问同一个变量n
#     for i in range(5):
#         t = threading.Thread(target=fn)
#         t.start()
#         # t.join()  # 同步


# 解决线程冲突
# 线程锁
lock = threading.Lock()
# rlock = threading.RLock()  # 递归锁


def fn2():
    # 自动加锁，自动释放锁
    with lock:
        global n
        for _ in range(1000000):
            n += 1
        print(n)

    # lock.acquire()  # 加锁
    # global n
    # for _ in range(1000000):
    #     n += 1
    # print(n)
    # lock.release()  # 解锁/释放锁


def thread_lock():
    for i in range(5):
        t = threading.Thread(target=fn2)
        t.start()

#
if __name__ == '__main__':
    # thread1()
    thread_lock()


# 线程锁：可以解决多个线程访问同一个资源的问题。
# 递归锁：解决线程死锁。

# 线程A    线程B
#   |       |
# 资源1    资源2
#
# 死锁：是指一个资源被多次调用，而多次调用方都未能释放该资源就会造成一种互相等待的现象，
#      若无外力作用，它们都将无法推进下去。此时称系统处于死锁状态或系统产生了死锁。
#      互相锁住对方线程需要的资源，造成死锁局面
#


