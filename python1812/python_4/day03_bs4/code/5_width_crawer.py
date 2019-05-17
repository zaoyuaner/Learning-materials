# #doc homework test
# #homework test stu
#  test stu vedio
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

def width_crawer(start_url):
    #队列模拟
    #入队列 append() 出队列pop()
    url_quene = []
    url_quene.append(start_url)
    while len(url_quene) > 0:
        url = url_quene.pop(0)
        print("\t" * deep_dict[url], "当前层级:%d" % deep_dict[url])
        if deep_dict[url] <= 3:
            #获取子url列表
            sonurl_list = get_son_url(url)
            for sonurl in sonurl_list:
                #过滤有效的链接
                if sonurl.startswith('http'):
                    #去重 为了不重复爬取
                    if sonurl not in deep_dict:
                        deep_dict[sonurl] = deep_dict[url]+1
                        url_quene.append(sonurl)



if __name__ == "__main__":
    url = "https://www.baidu.com/s?wd=苍老师"

    #将key 存放 url value存放层级 1 2 3
    deep_dict={} #这里边存放我们所有的列表
    deep_dict[url] = 1
    #开始爬取
    width_crawer(url)