from multiprocessing import Process, Pool
import time
import random
import os


def run(name):

    # 父进程id
    print('父进程id为: %s' % os.getppid())

    # 自己的id
    print(f'{name}的进程id: %s' % os.getpid())
    # 随机睡几秒
    time.sleep(random.choice([1,2,3]))
    print(f'{name}结束')


if __name__ == '__main__':
    print('父进程开始执行', os.getpid())
    # 创建进程池
    pool = Pool(4)

    # 往pool中添加进程
    for i in range(4):
        # 异步
        # pool.apply_async(run, args=(i, ))
        # 同步
        pool.apply(run, args=(i, ))

    # 关闭进程池
    pool.close()
    # 等待进程池中的进程跑完.
    pool.join()

    print('父进程结束')



