import time
import requests
import threading


# 模拟浏览器
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36"
}

sem = threading.Semaphore(10)  # 控制最多10个线程在运行
def get_page(page):
    '''
    获取每一页的数据
    '''
    with sem:
        url = 'https://sz.lianjia.com/ershoufang/pg%d/' % page

        response = requests.get(url, headers=headers)
        # print(response.text)
        print('第%d页' % page, len(response.text))


if __name__ == '__main__':

    start = time.time()

    t_list = []
    for i in range(1, 101):

        # 同步：不使用多线程
        # get_page(i)

        # 异步：使用多线程
        t = threading.Thread(target=get_page, args=(i,))
        t.start()

        t_list.append(t)

    for t in t_list:
        t.join()

    end = time.time()
    print(end - start)



