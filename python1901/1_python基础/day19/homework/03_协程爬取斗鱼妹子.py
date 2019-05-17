
# 使用协程爬取斗鱼妹子
import requests
import re
# url = "https://www.douyu.com/gapi/rknc/directory/yzRec/3"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36"
}
url = "https://www.douyu.com/gapi/rknc/directory/yzRec/1"
response = requests.get(url,headers = headers)
content = response.text
# print(content)
# p = open("ptoto.txt","w",encoding="utf-8")
# p.write(content)
pattern = '"https(.*?)",.*?"nn":"(.*?)",'
photo_list = re.findall(pattern,content,re.S)
# print(photo_list)

# photourl_list = []
for i,j in photo_list:
    photo_url = 'https'+i

    # url='https://rpic.douyucdn.cn/live-cover/appCovers/2019/03/09/6523500_20190309142516_small.jpg'
    res = requests.get(photo_url)
    with open('%s.jpg'%j, 'wb') as fp:
        fp.write(res.content)
        print("已打印%s"%j)
