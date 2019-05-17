import multiprocessing
from time import sleep


def fn(*args):
    sleep(1)
    print("子进程：", multiprocessing.current_process().name)
    print(args)


if __name__ == '__main__':
    p = multiprocessing.Process(target=fn, args=('波音737', '空客', 'C919'), name='埃塞俄比亚')
    p.start()
    p.join()  # 等待p进程结束

    p = multiprocessing.Process(target=fn, args=('波音737', '空客', 'C919'), name='埃塞俄比亚')
    p.start()
    print(p.name)
    print(p.pid)  # 进程id


