import json
import urllib.request

headers = {
"User-Agent":"User-Agent, Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"
}
for i in  range(100):
    url = "https://movie.douban.com/j/new_search_subjects?sort=T&range=0,10&tags=&start=%d"%(i)
    requests = urllib.request.Request(url,headers=headers)
    responses = urllib.request.urlopen(requests)
    content = responses.read().decode()
    #print(content) #json 数据

    data = json.loads(content)
    print(data)
    data_list = data.get('data')
    for movie in data_list:
        title = movie['title']
        casts = movie['casts']
        print("电影名：%s 主演:%s" %(title,casts))
