import requests
from lxml import etree
headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36"
}
url = 'https://movie.douban.com/cinema/nowplaying/shenzhen/'
#将 目标网站上的数据抓取下来
response = requests.get(url,headers=headers)
text = response.text #解码后的字符串  str类型
#response.content #类型是bytes

# 将抓取下来的数据根据一定的规则进行提取
html = etree.HTML(text)
ul = html.xpath("//ul[@class='lists']")[0]#返回的是列表
lis = ul.xpath("./li")

movies = [] #存放字典的列表  存放电影相关信息
for li in lis:
    title = li.xpath("@data-title")[0]
    score =li.xpath("@data-score")[0]
    star =li.xpath("@data-star")[0]
    duration =li.xpath("@data-duration")[0]
    region =li.xpath("@data-region")[0]
    director =li.xpath("@data-director")[0]
    actors =li.xpath("@data-actors")[0]
    thumbnail =li.xpath(".//img/@src")[0]
    movie = {
        "title":title,
        "score":score,
        "star":star,
        "duration":duration,
        "region":region,
        "director":director,
        "actors":actors,
        "thumbnail":thumbnail,
    }
    movies.append(movie)

print(movies)


