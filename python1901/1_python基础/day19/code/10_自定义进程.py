import multiprocessing
import os


class MyProcess(multiprocessing.Process):
    def __init__(self, name, url):
        super().__init__()
        self.name = name
        self.url = url

    def run(self):
        print('子进程', multiprocessing.current_process().name)  # 特朗普
        print('子进程', multiprocessing.current_process().pid)
        print('子进程', self.pid)
        print('子进程', os.getpid())  # 当前进程的id
        print('父进程', os.getppid())  # 当前进程的父进程id


if __name__ == '__main__':
    p = MyProcess('特朗普', 'www.baidu.com')
    p.start()

    print(os.getpid()) # 主进程id




