from threading import Thread


num = 100


def run():
    print('子线程 开始执行')
    global num
    num += 1
    print('num=', num)


if __name__ == '__main__':
    print('主线程开始执行')
    t = Thread(target=run)
    t.start()
    t.join()

    print('主线程: num=', num)
