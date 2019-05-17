import threading
import time
import random


def fn(*args):
    time.sleep(random.randint(1, 3))
    # print('子线程:', args)


if __name__ == '__main__':
    # 多个线程同时运行，是异步执行
    # t1 = threading.Thread(target=fn, args=('包贝尔',))
    # t1.start()
    # # t1.join()  # 会阻塞，等待t1线程执行完成后再往后执行。
    # t2 = threading.Thread(target=fn, args=('王祖蓝',))
    # t2.start()
    # # t2.join()
    # t3 = threading.Thread(target=fn, args=('宝强',))
    # t3.start()
    # # t3.join()

    start = time.time()

    t_list = []
    for i in range(1, 10):
        t = threading.Thread(target=fn, args=('赵公子-%d' % i,))
        t.start()
            # t.join()  # 同步
        t_list.append(t)

        # 线程的属性
        # print(t.name)  # t线程的名称
        # print(threading.current_thread().name)  # 当前线程的名称
        # print(t.daemon)  # 是否守护线程，默认是非守护
        # print(t.ident)  # 线程id
        # print(t.is_alive())  # t线程是否正在执行
        # print(threading.active_count())  # 正在运行的线程数量（包含主线程）
        # print(threading.enumerate())  # 枚举当前正在运行的所有线程

    # 等待所有线程全部执行完毕
    for t in t_list:
        t.join()

    end = time.time()
    print(end - start)



