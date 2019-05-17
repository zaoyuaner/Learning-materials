# Day05

## 多线程

在介绍Python中的线程之前，先明确一个问题，Python中的多线程是假的多线程！ 
为什么这么说，我们先明确一个概念，全局解释器锁（GIL）

#### 什么是GIL

```
Python代码的执行由Python虚拟机（解释器）来控制,同时只有一个线程在执行。对Python虚拟机的访问由全局解释器锁（GIL）来控制，正是这个锁能保证同时只有一个线程在运行。
```

#### 为什么要GIL

```
为了线程间数据的一致性和状态同步的完整性
```

#### GIL的影响

```python
只有一个线程在运行，无法使用多核。

在多线程环境中，Python虚拟机按照以下方式执行。
	1.设置GIL。
	2.切换到一个线程去执行。
	3.运行。
	4.把线程设置为睡眠状态。
	5.解锁GIL。
	6.再次重复以上步骤。

比方我有一个4核的CPU，那么这样一来，在单位时间内每个核只能跑一个线程，然后时间片轮转切换。
但是Python不一样，它不管你有几个核，单位时间多个核只能跑一个线程，然后时间片轮转。
执行一段时间后让出，多线程在Python中只能交替执性，10核也只能用到1个核

# 使用线程
from threading import Thread
def loop():
    while True:
        print("亲爱的，我错了，我能吃饭了吗?")

if __name__ == '__main__':
    for i in range(3):
        t = Thread(target=loop)
        t.start()
    while True:
        pass

# 而如果我们变成进程呢？cpu --100%
from multiprocessing import Process
def loop():
    while True:
        print("亲爱的，我错了，我能吃饭了吗?")

if __name__ == '__main__':
    for i in range(3):
        t = Process(target=loop)
        t.start()
    while True:
        pass
```

#### 多线程怎么使用多核

```
1、重写python编译器(官方cpython)如使用：PyPy解释器
2、调用C语言的链接库
```

#### cpu密集型(计算密集型)、I/O密集型

```
计算密集型任务由于主要消耗CPU资源，代码运行效率至关重要，C语言编写

IO密集型，涉及到网络、磁盘IO的任务都是IO密集型任务，这类任务的特点是CPU消耗很少，任务的大部分时间都在等待IO操作完成,99%的时间花费在IO上，脚本语言是首选，C语言最差。
```



### 创建多线程

```python
def doSth(arg):
    # 拿到当前线程的名称和线程号id
    threadName = threading.current_thread().getName()
    tid = threading.current_thread().ident
    for i in range(5):
        print("%s *%d @%s,tid=%d" % (arg, i, threadName, tid))
        time.sleep(2)
```

#### 1、使用_thread.start_new_thread开辟子线程

```python
def simpleThread():
    # 创建子线程，执行doSth
    # 用这种方式创建的线程为【守护线程】（主线程死去“护卫”也随“主公”而去）
    _thread.start_new_thread(doSth, ("拍森",))

    mainThreadName = threading.current_thread().getName()
    print(threading.current_thread())
    
    # 5秒的时间以内，能看到主线程和子线程在并发打印
    for i in range(5):
        print("劳资是主线程@%s" % (mainThreadName))
        time.sleep(1)

    # 阻塞主线程，以使【守护线程】能够执行完毕
    while True:
        pass
```

#### 2、 通过创建threading.Thread对象实现子线程

```python
def threadingThread():
    # 默认不是【守护线程】
    t = threading.Thread(target=doSth, args=("大王派我来巡山",)) # args=(,) 必须是元组
    # t.setDaemon(True)  # 设置为守护线程
    t.start()  # 启动线程，调用run()方法
    
```

#### 3、通过继承threading.Thread类，进而创建对象实现子线程

```python
class MyThread(threading.Thread):
    def __init__(self, name, task, subtask):
        super().__init__()

        self.name = name  # 覆盖了父类的name
        self.task = task  # MyThread自己的属性
        self.subtask = subtask  # MyThread自己的属性

    # 覆写父类的run方法，
    # run方法以内为【要跑在子线程内的业务逻辑】(thread.start()会触发的业务逻辑)
    def run(self):
        for i in range(5):
            print("【%s】并【%s】 *%d @%s" % (self.task, self.subtask, i, threading.current_thread().getName()))
            time.sleep(2)

def classThread():
    mt = MyThread("小分队I", "巡山", "扫黄")
    mt.start()  #  启动线程

```

#### 4、几个重要的API

````python
def importantAPI():
    print(threading.currentThread())  # 返回当前的线程变量
    # 创建五条子线程
    t1 = threading.Thread(target=doSth, args=("巡山",))
    t2 = threading.Thread(target=doSth, args=("巡水",))
    t3 = threading.Thread(target=doSth, args=("巡鸟",))

    t1.start()  # 开启线程
    t2.start()
    t3.start()

    print(t1.isAlive())  # 返回线程是否活动的
    print(t2.isDaemon())  # 是否是守护线程
    print(t3.getName())  # 返回线程名
    t3.setName("巡鸟")  # 设置线程名
    print(t3.getName())
    print(t3.ident)  # 返回线程号

    # 返回一个包含正在运行的线程的list
    tlist = threading.enumerate()
    print("当前活动线程：", tlist)

    # 返回正在运行的线程数量（在数值上等于len(tlist)）
    count = threading.active_count()
    print("当前活动线程有%d条" % (count))

````



#### 线程冲突

```python
'''
【线程冲突】示例：
	多个线程并发访问同一个变量而互相干扰
'''
import threading
import time
money = 0

# CPU分配的时间片不足以完成一百万次加法运算，
# 因此结果还没有被保存到内存中就被其它线程所打断
def addMoney():
    global money
    for i in range(1000000):
        money += 1
    print(money)


# 创建线程锁
lock = threading.Lock()

def addMoneyWithLock():
    # print("addMoneyWithLock")
    time.sleep(1)
    global money
    # print(lock.acquire())
    # if lock.acquire():
    #     for i in range(1000000):
    #         money += 1
    # lock.release()
    # 独占线程锁
    with lock:  # 阻塞直到拿到线程锁

        # -----下面的代码只有拿到lock对象才能执行-----
        for i in range(1000000):
            money += 1
        # 释放线程锁，以使其它线程能够拿到并执行逻辑
        # ----------------锁已被释放-----------------

    print(money)

# 5条线程同时访问money变量，导致结果不正确
def conflictDemo():
    for i in range(5):
        t = threading.Thread(target=addMoney)
        t.start()

# 通过线程同步（依次执行）解决线程冲突
def handleConflictBySync():
    for i in range(5):
        t = threading.Thread(target=addMoney)
        t.start()
        t.join()  # 一直阻塞到t运行完毕

# 通过依次独占线程锁解决线程冲突
def handleConflictByLock():
    # 并发5条线程
    for i in range(5):
        t = threading.Thread(target=addMoneyWithLock)
        t.start()

if __name__ == '__main__':
    # conflictDemo()
    # handleConflictBySync()
    handleConflictByLock()

    pass
```

#### 死锁

```
死锁：是指一个资源被多次调用，而多次调用方都未能释放该资源就会造成一种互相等待的现象，若无外力作用，它们都将无法推进下去。此时称系统处于死锁状态或系统产生了死锁。

互相锁住对方线程需要的资源，造成死锁局面
```

#### 线程安全

##### 互斥锁

```python
互斥锁
    状态：锁定/非锁定
    # 创建锁
        lock = threading.Lock()
    # 锁定
        lock.acquire()
    # 释放
        lock.release()
```

##### 递归锁

```python
递归锁，重用锁，用于解决死锁的问题,可重复锁

# 递归锁
rlock = threading.RLOCK()

```



####  信号量Semaphore调度线程：控制最大并发量

```python
'''
使用Semaphore调度线程：控制最大并发量
'''
import threading
import time

# 允许最大并发量3
sem = threading.Semaphore(3)

def doSth(arg):
    with sem:
        tname = threading.current_thread().getName()
        print("%s正在执行【%s】" % (tname, arg))
        time.sleep(1)
        print("-----%s执行完毕!-----\n" % (tname))
        time.sleep(0.1)

if __name__ == '__main__':

    # 开启10条线程
    for i in range(10):
        threading.Thread(target=doSth, args=("巡山",), name="小分队%d" % (i)).start()
    

```



## 协程

```
协程，又称微线程，纤程。英文名Coroutine。
首先我们得知道协程是啥？协程其实可以认为是比线程更小的执行单元。为啥说他是一个执行单元，因为他自带CPU上下文。这样只要在合适的时机，我们可以把一个协程切换到另一个协程,只要这个过程中保存或恢复CPU上下文那么程序还是可以运行的。

通俗的理解：在一个线程中的某个函数，可以在任何地方保存当前函数的一些临时变量等信息，然后切换到另外一个函数中执行，注意不是通过调用函数的方式做到的，并且切换的次数以及什么时候再切换到原来的函数都由开发者自己确定。
```

#### 协程和线程差异

```python
协程的特点在于是一个线程执行， 那和多线程比，协程有何优势？
	1.最大的优势就是协程极高的执行效率。因为子程序切换不是线程切换，而是由程序自身控制，因此，没有线程切换的开销，和多线程比，线程数量越多，协程的性能优势就越明显。
	2.第二大优势就是不需要多线程的锁机制，因为只有一个线程，也不存在同时写变量冲突，在协程中控制共享资源不加锁，只需要判断状态就好了，所以执行效率比多线程高很多。

因为协程是一个线程执行，那怎么利用多核CPU呢？
	最简单的方法是多进程+协程，既充分利用多核，又充分发挥协程的高效率，可获得极高的性能。
	
协程的缺点： 它不能同时将CPU的多个核用上，只能使用一个核

Python对协程的支持是通过generator实现的。
在generator中，我们不但可以通过for循环来迭代，还可以不断调用next()函数获取由yield语句返回的下一个值。

# 协程一个简单实现
def C():
    while True:
        print("=====C=====")
        yield
        time.sleep(0.5)

def D(c):
    while True:
        print("=====D=====")
        next(c)
        time.sleep(0.5)

if __name__ == "__main__":
    c = C()
    D(c)
```



### 使用协程

#### 1.使用greenlet + switch实现协程调度

```python
'''
	使用greenlet + switch实现协程调度
'''
from greenlet import greenlet
import time


def func1():
    print("开门走进卫生间")
    time.sleep(3)
    gr2.switch()  # 把CPU执行权交给gr2

    print("飞流直下三千尺")
    time.sleep(3)
    gr2.switch()
    pass


def func2():
    print("一看拖把放旁边")
    time.sleep(3)
    gr1.switch()

    print("疑是银河落九天")
    pass


if __name__ == '__main__':
    gr1 = greenlet(func1)
    gr2 = greenlet(func2)
    gr1.switch()  # 把CPU执行权先给gr1
    pass

```

#### 2.使用gevent +sleep自动将CPU执行权分配给当前未睡眠的协程

```python
'''
	使用gevent +　sleep自动将CPU执行权分配给当前未睡眠的协程
'''
import gevent

def func1():
    gevent.sleep(1)
    print("大梦谁先觉")

    gevent.sleep(13)
    print("1:over")
    pass

def func2():
    gevent.sleep(3)
    print("平生我自知")

    gevent.sleep(9)
    print("2:over")
    pass

def func3():
    gevent.sleep(5)
    print("草堂春睡足")

    gevent.sleep(5)
    print("3:over")
    pass

def func4():
    gevent.sleep(7)
    print("窗外日迟迟")

    gevent.sleep(1)
    print("4:over")
    pass

def simpleGevent():
    gr1 = gevent.spawn(func1)
    gr2 = gevent.spawn(func2)
    gr3 = gevent.spawn(func3)
    gr4 = gevent.spawn(func4)
    gevent.joinall([
        gr1, gr2, gr3, gr4
    ])

if __name__ == '__main__':
    simpleGevent()
    
```

#### 3.通过monkey调度

```python
'''
	使用gevent +　monkey.patch_all()自动调度网络IO协程
'''
import gevent
from gevent import monkey
monkey.patch_all()  # 将【标准库-阻塞IO实现】替换为【gevent-非阻塞IO实现】

import requests
import time

def getPageText(url, order=0):
    print("No%d:%s请求开始..." % (order, url))
    resp = requests.get(url)  # 发起网络请求，返回需要时间——阻塞IO

    html = resp.text
    print("No%d:%s成功返回：长度为%d" % (order, url, len(html)))
    pass

if __name__ == '__main__':
    start = time.time()
    time.clock()
    gevent.joinall([
        gevent.spawn(getPageText, "http://www.sina.com", order=1),
        gevent.spawn(getPageText, "http://www.qq.com", order=2),
        gevent.spawn(getPageText, "http://www.baidu.com", order=3),
        gevent.spawn(getPageText, "http://www.163.com", order=4),
        gevent.spawn(getPageText, "http://www.4399.com", order=5),
        gevent.spawn(getPageText, "http://www.sohu.com", order=6),
        gevent.spawn(getPageText, "http://www.youku.com", order=7),
        gevent.spawn(getPageText, "http://www.iqiyi.com", order=8),
    ])

    end = time.time()
    print("over，耗时%d秒" % (end - start))
    print(time.clock())
    
```


