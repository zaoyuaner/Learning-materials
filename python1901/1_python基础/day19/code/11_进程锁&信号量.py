import multiprocessing
import time



# 信号量：控制进程的最大并发数
def fn(i, sem):
    with sem:
        print("子进程开始", i)
        time.sleep(3)
        print('结束', i)


# 进程锁
def fn2(i, lock):
    with lock:
        print('第%d个进程加锁' % i)
        time.sleep(3)
        print('第%d个进程释放锁' % i)


if __name__ == '__main__':
    sem = multiprocessing.Semaphore(4)
    # for i in range(1, 21):
    #     p = multiprocessing.Process(target=fn, args=(i, sem))
    #     p.start()

    lock = multiprocessing.Lock()
    for i in range(1, 5):
        p = multiprocessing.Process(target=fn2, args=(i, lock))
        p.start()




