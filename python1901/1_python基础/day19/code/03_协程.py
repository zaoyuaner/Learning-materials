
# 复习
#   GIL：全局解释器锁，
#     作用：只允许一个线程通过，所有Python中的多线程是假的
#   进程：系统分配的一个资源单位
#   线程：进程中的一个分支，进程中至少有一个主线程
#   多线程： 多个线程并发的一种技术
#   同步：按顺序执行
#   异步：可以理解为在不同的线程中独立执行
#   并行：任务数 <= CPU数
#   并发: 任务数 > CPU数
#
#   线程锁/互斥锁: threading.Lock，解决线程冲突
#   死锁：多个线程同一时刻占用资源不愿意释放，又想占用对方的资源，造成相互等待的现象
#   递归锁：threading.RLock, 解决死锁
#
#   信号量：控制线程的最大并发数


import time

# 协程一个简单实现
# C函数是生成器函数
def C():
    while True:
        print("=====C=====")
        yield
        time.sleep(0.5)

# D函数是普通函数
def D(c):
    while True:
        print("=====D=====")
        next(c)
        time.sleep(1)


if __name__ == "__main__":
    c = C()
    # print(c)  # <generator object C at 0x00000215E7851F68>
    # next(c)

    D(c)




