from multiprocessing import Process
from time import sleep


def run():
    print('子进程启动')
    sleep(3)
    print('子进程结束')


if __name__ == '__main__':
    print('父进程启动')
    p = Process(target=run)

    p.start()
    p.join(timeout=3)
    print('父进程结束')
