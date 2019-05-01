# 多线程爬取51job全部城市岗位，并分别保存到单独的以城市名为文件名的html中，如: 深圳.html
# url = "https://jobs.51job.com/"
import time
import requests
import re
import threading

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36"
}


def get_city():
    url = "https://jobs.51job.com/"
    res = requests.get(url, headers=headers)
    content = res.text

    pattern = '主要城市(?:.*?)<div class="lkst">(.*?)</div>'
    city_list = re.findall(pattern, content, re.S)
    # print(len(city_list))
    # print(city_list[0])
    city_str = city_list[0]

    url_pattern = 'href="(.*?)"'
    url_list = re.findall(url_pattern, city_str, re.S)

    name_pattern = '<a(?:.*?)>(.*?)</a>'
    name_list = re.findall(name_pattern, city_str, re.S)

    return url_list, name_list


def get_data(url, city):
    response = requests.get(url, headers=headers)

    path = r'./51job/%s.html' % city
    with open(path, 'wb') as fp:
        fp.write(response.content)


if __name__ == '__main__':
    url_list, city_list = get_city()

    s = time.time()
    t_list = []
    for i in range(len(url_list)):
        url = url_list[i]
        city = city_list[i]

        # 同步
        # get_data(url, city)

        # 异步
        t = threading.Thread(target=get_data, args=(url, city))
        t.start()
        t_list.append(t)

    for t in t_list:
        t.join()

    e = time.time()
    print(e - s)