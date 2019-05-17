#encoding:utf-8
import threading
import time
# def coding():
#     for x in range(3):
#         print("%s 正在写代码" %x)
#         time.sleep(1)
#
# def drawing():
#     for x in range(3):
#         print("%s 正在画图:" %x)
#         time.sleep(1)
#
# def main():
#     coding()
#     drawing()
#
# if __name__ == "__main__":
#     main()

#以上用了 6秒  采用多线程的方式 多件事情一起做

def coding():
    for x in range(3):
        print("%s 正在写代码" % threading.current_thread())
        time.sleep(1)
def drawing():
    for x in range(3):
        print("%s 正在画图" % threading.current_thread())
        time.sleep(1)

def main():
    t1 = threading.Thread(target=coding) #开辟一个线程 参数是让他干嘛
    t2 = threading.Thread(target=drawing)

    t1.start() #开始线程
    t2.start()

    print(threading.enumerate())#查看线程的数量
if __name__ == "__main__":
     main()

