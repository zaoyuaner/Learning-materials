from threading import Thread, local


num = 100

thread_local = local()


def foo(x, n):
    x += n
    x -= n


def run(n):
    global num
    global thread_local
    thread_local.x = num
    for i in range(1000000):
        foo(thread_local.x, n)
    print('thread_local.x', thread_local.x)

if __name__ == '__main__':
    print('主线程开始执行')
    t1 = Thread(target=run, args=(6,))
    t2 = Thread(target=run, args=(8,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print('num=', num)
    # print('thread_local.x', thread_local.x)
