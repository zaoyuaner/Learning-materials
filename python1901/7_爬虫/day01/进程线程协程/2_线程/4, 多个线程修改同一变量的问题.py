from threading import Thread, Lock


num = 100
lock = Lock()

def run(n):
    global num
    global lock
    for i in range(1000000):
        # try:
        #     num += n
        #     num -= n
        # except:
        #     pass
        # finally:
        #     lock.release()
        # 推荐写法
        with lock:
            num +=  n
            num -=  n


if __name__ == '__main__':
    t1 = Thread(target=run, args=(6,))
    t1.start()

    t2 = Thread(target=run, args=(8,))
    t2.start()

    t1.join()
    t2.join()

    print('num=', num)
