import gevent
from gevent import monkey
monkey.patch_all()

import time
import requests


# 模拟浏览器
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36"
}

def get_page(page):
    url = 'https://sz.lianjia.com/ershoufang/pg%d/' % page
    response = requests.get(url, headers=headers)
    # print('第%d页' % page, len(response.text))
    print('第%d页' % page)


if __name__ == '__main__':

    start = time.time()

    g_list = []
    for i in range(0, 300):
        g = gevent.spawn(get_page, i%100+1)
        g_list.append(g)
    gevent.joinall(g_list)

    end = time.time()
    print(end - start)



