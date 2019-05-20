from time import sleep
from multiprocessing import Process


# 任务一
def run(desc):
    while True:
       print(f'{desc} day')
       sleep(1.2)



if __name__ == '__main__':

    # 新建一个进程
    # p = Process(target=run, args=('hot and moist',))
    p = Process(target=run, kwargs={'desc': 'hot and moist'})
    p.start()
    # 任务二

    while True:
        print('good day')
        sleep(1)

    # 只有上面的while循环结束才会执行到run
    # run()
