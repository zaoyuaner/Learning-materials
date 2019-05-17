#encoding:utf-8
import threading
import time
import random
gMoney = 1000
#如果你的程序中 两个线程都会操作全局变量 那么记得上锁
gCondition = threading.Condition()
gTotalTimes = 10 #这是总的次数
gTime = 0  #生产一次或者消费一次  加1
class ProducerThread(threading.Thread):
    def run(self):
        global gMoney
        global gTime
        while True:
            money = random.randint(100,1000)
            gCondition.acquire()
            if gTime >= gTotalTimes:
                gCondition.release()
                break
            gMoney += money
            print("%s生产了%d元钱，余额%d元钱" %(threading.current_thread(),money,gMoney))
            gTime +=1
            gCondition.notify_all()#一定要在释放之前通知正在等待的线程
            gCondition.release()
            time.sleep(1)


class CustomerThread(threading.Thread):
    def run(self):
        global gMoney
        while True:
            money = random.randint(100,1000)
            gCondition.acquire()
            #if  if条件判断完了以后执行下面的语句
            #while while条件判断完了以后 回来还要再判断一次
            while gMoney < money:
                if gTime >= gTotalTimes:
                    gCondition.release()
                    return
                print("%s准备消费%d元钱，剩余%d元钱，余额不足" % (threading.current_thread(), money, gMoney))
                gCondition.wait()
            gMoney -= money
            print("%s消费了%d元钱，剩余%d元钱" % (threading.current_thread(), money, gMoney))
            gCondition.release()
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
