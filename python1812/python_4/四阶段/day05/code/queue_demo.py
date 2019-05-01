#encoding:utf-8

from queue import Queue
import threading
import time
# q = Queue(4)
#
# for x in range(4):
#     q.put(x)
#
# for x in range(4):
#     print(q.get())
# print(q.qsize())
# print(q.full())
# print(q.empty())

def set_value(q):
    index = 0
    while True:
        q.put(index)#如果满了 会处于阻塞状态
        index +=1
        time.sleep(3)
def get_value(q):
    while True:
        print(q.get()) #如果为空那么就处于 阻塞状态
        time.sleep(5)

def main():
    q = Queue(4)
    t1 = threading.Thread(target=set_value,args=[q])
    t2 = threading.Thread(target=get_value,args=[q])
    t1.start()
    t2.start()

if __name__ == "__main__":
    main()