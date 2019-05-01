
# 使用多线程爬取深圳所有区的房源，并分别保存到单独的以区为文件名的html中，如: 南山区.html
# （爬取每个区的第一页即可）
# https://sz.lianjia.com/ershoufang/pg1/
import time
import requests
import re
import threading

# 模拟浏览器
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36"
}

# 获取所有区
def get_area():
    url = 'https://sz.lianjia.com/ershoufang/pg1/'
    response = requests.get(url, headers=headers)
    content = response.text

    pattern = '<div data-role="ershoufang" >(.*?)</div>'
    area_str = re.findall(pattern, content, re.S)[0]
    # print(area_str)

    url_pattern = 'href="(.*?)"'
    url_list = re.findall(url_pattern, area_str, re.S)
    # print(url_list)

    areaname_pattern = '<a(?:.*?)>(.*?)</a>'
    areaname_list = re.findall(areaname_pattern, area_str, re.S)
    # print(areaname_list)

    return url_list, areaname_list


def get_data(url, area):
    response = requests.get(url, headers=headers)

    path = r'./lianjia/%s.html' % area
    with open(path, 'wb') as fp:
        fp.write(response.content)


if __name__ == '__main__':

    url_list, area_list = get_area()

    s = time.time()
    t_list = []
    for i in range(len(url_list)):
        url = 'https://sz.lianjia.com' + url_list[i]
        area = area_list[i]

        # 同步
        # get_data(url, area)

        # 异步
        t = threading.Thread(target=get_data, args=(url, area))
        t.start()
        t_list.append(t)

    for t in t_list:
        t.join()

    e = time.time()
    print(e - s)

