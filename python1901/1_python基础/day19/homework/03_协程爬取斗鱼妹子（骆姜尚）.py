# 使用协程爬取斗鱼妹子
# url = "https://www.douyu.com/gapi/rknc/directory/yzRec/3"

import os
import re
import time
import requests
import threading


# 获取网页
def get_url(i, url):
    # 拼接url
    Url = url + str(i)

    # print(Url)
    # 获取json数据
    res = requests.get(Url)
    # 获取图片地址和主播名字
    lian_name_list = re.findall(r'"rs16":"(.*?\.jpg)",".*?"nn":"(.*?)","', res.text)
    # 写入保存
    for url2, name in lian_name_list:
        jpg_url = requests.get(url2)
        with open(r'斗鱼第%s页/%s.jpg' % (i,name), 'wb') as fp:
            fp.write(jpg_url.content)
            print('%s_%s.jpg' % (i,name))

def get_area(url, area):
    # 使用协程
    t_list = []
    for i in range(1, 101):
        t = threading.Thread(target=get_page, args=(i, url, area))
        t.start()
        t_list.append(t)

    for t in t_list:
        t.join()

if __name__ == '__main__':
    s = time.time()
    url = "https://www.douyu.com/gapi/rknc/directory/yzRec/"
    #创建协程
    t_list = []
    for i in range(1, 10):
        #创建文件夹存放
        os.mkdir("斗鱼第%s页"%i)
        t = threading.Thread(target=get_url, args=(i, url))
        t.start()
        t_list.append(t)

    for t in t_list:
        t.join()

    e = time.time()
    print(e-s)
