import threading
import time

# 信号量：控制线程的最大并发数
sem = threading.Semaphore(4)


def fn(*args):
    with sem:
        print('子线程:', args)
        time.sleep(3)
        print('结束：', args)


if __name__ == '__main__':
    for i in range(1,21):
        t = threading.Thread(target=fn, args=('thread-%d' % i, ))
        t.start()



