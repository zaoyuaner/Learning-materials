import gevent
from gevent import monkey
monkey.patch_all()

# 使用协程爬取斗鱼妹子
# url = "https://www.douyu.com/gapi/rknc/directory/yzRec/3"

import requests
import pprint


def spider_douyu(page):
    url = "https://www.douyu.com/gapi/rknc/directory/yzRec/%d" % page
    res = requests.get(url)
    # pprint.pprint(res.json())

    rl_list = res.json().get('data').get('rl')
    for rl in rl_list:
        name = rl.get('nn')
        img_url = rl.get('rs1')
        save_meizi(name, img_url)


def save_meizi(name, url):
    res = requests.get(url)
    with open('./douyu/%s.png' % name, 'wb') as fp:
        fp.write(res.content)


if __name__ == '__main__':

    g_list = []
    for page in range(1, 6):
        # spider_douyu(page)
        g = gevent.spawn(spider_douyu, page)
        g_list.append(g)
    gevent.joinall(g_list)
