import gevent
from gevent import monkey  # 导入猴子补丁
monkey.patch_all()  # 可以实现协程的自动切换

import requests
import time

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36"
}


def get_data(url):
    print('协程：', url)

    response = requests.get(url, headers=headers)
    print(url, 'response:', len(response.text))


if __name__ == '__main__':
    url_list = [
        'http://www.baidu.com',
        'http://www.qq.com',
        'http://www.ifeng.com',
        'http://www.sina.com.cn',
        'http://www.taobao.com',
    ]

    # 创建协程
    s = time.time()

    g_list = []
    for url in url_list:
        # 同步
        # get_data(url)

        g = gevent.spawn(get_data, url)
        g_list.append(g)


    gevent.joinall(g_list)  # 执行所有协程

    e = time.time()
    print(e - s)





