from lxml import etree
import requests
BASE_DOMAIN = 'https://www.dytt8.net'
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36"
}

def parse_detail_page(url):
    movie = {}
    response = requests.get(url, headers=HEADERS)
    text = response.content.decode('gbk')
    html = etree.HTML(text)
    title = html.xpath("//*[@id='header']/div/div[3]/div[3]/div[2]/div[2]/div[1]")[0]
    movie['title'] = title
    zoomE = html.xpath("//div[@id='Zoom']")[0]
    imgs = zoomE.xpath(".//img/@src")
    cover = imgs[0]
    screenshot = imgs[1]
    movie['cover'] = cover
    movie['screenshot'] = screenshot

    infos = zoomE.xpath(".//text()")
    def parse_info(info,rule):
        return info.replace(rule,"").strip()
    for info in infos:
        if info.startwitch("◎年　　代"):
            info = parse_info(info,"◎年　　代")
        elif info.startwitch("◎产　　地"):
            info = parse_info(info, "◎产　　地")

def get_detail_urls(url):
    response = requests.get(url,headers=HEADERS)
    text = response.text
    # requests库使用自己猜测的编码方式给你解码 ISO
    #response.content.decode('gbk') 一般我们会使用这种
    #我们仅仅是抓取url 内容不怎么影响所以 text 即可
    html = etree.HTML(text)
    detail_urls = html.xpath("//table[@class='tbspan']//a/@href")
    detail_urls =list(map(lambda url:BASE_DOMAIN+url,detail_urls))
    #map() 每个元素做同样的事情
    # def abc(url):
    #     return BASE_DOMAIN+url
    # for detail_url in detail_urls:
    #     detail_url = abc(detail_url)
    #     detail_urls[index] = detail_url
    #     index+=1
    return detail_urls


def spider():
     base_url = 'https://www.dytt8.net/html/gndy/dyzz/list_23_{}.html'
     movies = []
     #第一层循环是控制爬七个页面
     for x in range(1,8):
         #构建完整的url
         url = base_url.format(x)
         #拿到每一页的列表
         detial_urls = get_detail_urls(url)
         #第二个for循环遍历 一页中的详情url
         # for detial_url in detial_urls:
         #     movie =parse_detail_page(detial_url)
         #     movies.append(movie)




     # print(movies)
if __name__ == "__main__":
    spider()