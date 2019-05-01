#encoding:utf-8
import threading
VALUE = 0

def add_value():
    global VALUE
    for x in range(1000000):
        VALUE+=1
    print("value:%d" % VALUE)

    # 本来打印的数据应该是  1000000 2000000  但是返回的是 1211234 1442345 并不是我们想要的
    #想要解决这个问题 加锁  第一个线程在操作 全局变量 上锁  另外一个想操作 可以 先等着释放锁 拿到之后才执行
def main():
    for x in range(2):
        t = threading.Thread(target=add_value)
        t.start()

if __name__ == "__main__":
     main()
