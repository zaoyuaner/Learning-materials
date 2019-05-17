# 获取页面的子列表  首先先获取内容
#然后匹配出a标签中的href

import re
import requests
headers = {
 "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
}
#获取网页内容
def get_content(url):
    try:
        res = requests.get(url,headers=headers)
        return res.text
    except:
        return ""
#获取子url列表
def get_son_url(url):
     contentes = get_content(url) #页面的内容
     href_re = '<a.*?href="(.*?)".*?>'
     href_list = re.findall(href_re,contentes,re.S)
     return href_list
def deep_crawer(url):

    if deep_dict[url]>3:
        return
    print("+"*20)
    print("\t"*deep_dict[url],"当前层级:%d" %deep_dict[url])
    son_list = get_son_url(url)
    for sonurl in son_list:
        #列表中http开头的就是有效的
        if sonurl.startswith('http'):
            #去重
            if sonurl not in deep_dict:
                #子url的层级就是父url的层级+1
                deep_dict[sonurl] = deep_dict[url] + 1
                deep_crawer(sonurl)

if __name__ == "__main__":
    url = "https://www.baidu.com/s?wd=岛国教育片"

    #将key 存放 url value存放层级 1 2 3
    deep_dict={} #这里边存放我们所有的列表
    deep_dict[url] = 1
    #开始爬取
    deep_crawer(url)