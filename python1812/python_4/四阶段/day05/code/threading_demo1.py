#encoding:utf-8
import threading
import time

class CodingThread(threading.Thread):
    def run(self): # 原来创建进程是:threading.Thread(target=) 现在当实例化的时候 会自动调用run方法
        for x in range(3):
            print("%s 正在写代码" % threading.current_thread())
            time.sleep(1)

class DrawingThread(threading.Thread):
    def run(self):
        for x in range(3):
            print("%s 正在画图" % threading.current_thread())
            time.sleep(1)
def main():
    t1 = CodingThread()  #创建了两个线程
    t2 = DrawingThread()
    t1.start()
    t2.start()
if __name__ == "__main__":
     main()
