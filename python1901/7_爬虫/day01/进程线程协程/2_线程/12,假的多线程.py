from threading import Thread


def loop():
    while True:
        print("亲爱的，我错了，我能吃饭了吗?")


if __name__ == '__main__':

    for i in range(3):
        t = Thread(target=loop)
        t.start()
