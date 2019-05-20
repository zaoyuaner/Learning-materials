from multiprocessing import Process
from time import sleep

# 定义全局变量
num = 100

# 子进程
def run():
    print('开始执行子进程')
    # 引入全局变量
    global  num
    # 修改全局变量
    num += 1
    print(num)
    print('子进程结束')


if __name__ == '__main__':
    print('父进程开始')

    p = Process(target=run)
    p.start()
    p.join()
    print('父进程结束--%d'%num)
