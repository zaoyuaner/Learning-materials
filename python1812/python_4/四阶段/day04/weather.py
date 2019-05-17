#pip install pyecharts

import requests
from bs4 import BeautifulSoup
from pyecharts import Bar
ALL_DATA = []  #新建一个容器 用来存放所有的城市和温度
def parse_page(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36"
    }
    response = requests.get(url,headers=headers)
    text = response.content.decode('utf-8')
    #pip install html5lib
    soup = BeautifulSoup(text,'html5lib')
    conMidtab=soup.find('div',class_='conMidtab')
    tables = conMidtab.find_all('table')
    for table in tables:
        trs = table.find_all('tr')[2:]
        for index,tr in enumerate(trs):
            tds = tr.find_all('td')
            city_td = tds[0] #获取列表
            #print(city_td)
            if index == 0:
                city_td = tds[1]
            # print(city_td)
            city = list(city_td.stripped_strings)[0]
            temp_ed = tds[-2]
            temp_max = list(temp_ed.stripped_strings)[0]
            ALL_DATA.append({"city": city, "max_temp": int(temp_max)})
            # print({"city":city,"max_temp":temp_max})
def main():
    urls = [
        'http://www.weather.com.cn/textFC/db.shtml',
        'http://www.weather.com.cn/textFC/hb.shtml',
        'http://www.weather.com.cn/textFC/xb.shtml',
        'http://www.weather.com.cn/textFC/hd.shtml',
        'http://www.weather.com.cn/textFC/xn.shtml',
        'http://www.weather.com.cn/textFC/hn.shtml',
        'http://www.weather.com.cn/textFC/hz.shtml',
        'http://www.weather.com.cn/textFC/gat.shtml',
    ]

    for url in urls:
        parse_page(url)
    ALL_DATA.sort(key=lambda data:data['max_temp'])
    print(ALL_DATA)
    data = ALL_DATA[0:10]
    cities = list(map(lambda x:x['city'],data))
    max_temp =  list(map(lambda x:x['max_temp'],data))
    #实例化Bar对象
    charts = Bar("中国最低气温排行榜")
    charts.add('',cities,max_temp)#传值
    charts.render('temp.html') #将数据渲染到页面上
if __name__ == "__main__":
    main()

    # ALL_DATA = [
    #     {"city": "北京", "max_temp": 10},
    #     {"city": "上海", "max_temp": 7},
    #     {"city": "广州", "max_temp": 20},
    #     {"city": "深圳", "max_temp": 19},
    # ]
    # ALL_DATA.sort(key=lambda data: data['max_temp'])
    # print(ALL_DATA)