from greenlet import greenlet
import time


def fn1():
    print("协程1")
    time.sleep(3)
    g2.switch()  # 切换到协程g2

    print('C罗帽子戏法')
    time.sleep(3)
    g2.switch()


def fn2():
    print('协程2')
    time.sleep(3)
    g1.switch()  # 切换到协程g1

    print('梅西')
    time.sleep(3)


if __name__ == '__main__':
    g1 = greenlet(fn1)
    g2 = greenlet(fn2)
    g1.switch()  # 切换到g1协程





