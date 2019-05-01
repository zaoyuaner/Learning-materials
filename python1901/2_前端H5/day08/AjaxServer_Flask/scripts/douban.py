import requests
import json

headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
}


def get_movie(page):
    url = "https://movie.douban.com/j/new_search_subjects?sort=T&range=0,10&tags=&start=%d" % page

    res = requests.get(url, headers=headers)
    content = res.text

    # json解析
    content_dic = json.loads(content)
    movie_list = content_dic.get('data')

    # 遍历所有的电影
    title_list = []
    for movie in movie_list:
        title = movie.get('title')
        title_list.append(title)
    return title_list


if __name__ == '__main__':
    # 翻页爬取
    data_list = []
    for i in range(5):
        title_list = get_movie(page=i*20)
        data_list.append({'movie': title_list})

    with open('movies.json', 'w') as fp:
        fp.write(json.dumps(data_list))

