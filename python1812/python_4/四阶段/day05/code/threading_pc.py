#encoding:utf-8
import threading
import time
import random
gMoney = 1000
#如果你的程序中 两个线程都会操作全局变量 那么记得上锁
gLock = threading.Lock()
gTotalTimes = 10 #这是总的次数
gTime = 0  #生产一次或者消费一次  加1
class ProducerThread(threading.Thread):
    def run(self):
        global gMoney
        global gTime
        while True:
            money = random.randint(100,1000)
            gLock.acquire()
            if gTime >= gTotalTimes:
                gLock.release()
                break
            gMoney += money
            print("%s生产了%d元钱，余额%d元钱" %(threading.current_thread(),money,gMoney))
            gTime +=1
            gLock.release()
            time.sleep(1)


class CustomerThread(threading.Thread):
    def run(self):
        global gMoney
        while True:
            gLock.acquire()
            money = random.randint(100,1000)
            if gMoney >= money:
                gMoney -= money
                print("%s消费了%d元钱，剩余%d元钱" %(threading.current_thread(),money,gMoney))
            else:
                if gTime >= gTotalTimes:
                    gLock.release()
                    break
                print("%s准备消费%d元钱，剩余%d元钱，余额不足" % (threading.current_thread(), money, gMoney))
            gLock.release()
            time.sleep(1)
def main():
    for x in  range(3):
        t = CustomerThread(name="消费者线程%d"%x)
        t.start()

    for x in range(5):
        t = ProducerThread(name="生产者线程%d" % x)
        t.start()
if __name__ == "__main__":
     main()
