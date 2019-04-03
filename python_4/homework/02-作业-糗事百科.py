import re
import time
import urllib
from urllib import request

# 作业2: 爬取糗事百科文本页的所有段子,结果如 : xx说: xxxx
# https://www.qiushibaike.com/text/page/1/   # 1表示页码

# 正则表达式提示： 
#	# 获取一个评论
#   regCom = re.compile('<div class="author clearfix">(.*?)<span class="stats-vote"><i class="number">', re.S)
#	# 获取名称
#   nameCom = re.compile('<h2>(.*?)</h2>', re.S)
#	# 获取内容
#	contentCom = re.compile('<span>(.*?)</span>', re.S)

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36"
}


def getData(url):

    req = request.Request(url, headers=headers)
    res = request.urlopen(req)
    html = res.read().decode()
    # print(html)

    # 获取一个评论
    regCom = re.compile('<div class="author clearfix">(.*?)<span class="stats-vote"><i class="number">', re.S)
    comment_list = regCom.findall(html)

    # 遍历每一条评论
    item_list = []
    for comment in comment_list:

        # 获取名称
        nameCom = re.compile('<h2>(.*?)</h2>', re.S)
        name = nameCom.findall(comment)[0].strip()
        # 获取内容
        contentCom = re.compile('<span>(.*?)</span>', re.S)
        content = contentCom.findall(comment)[0].strip()

        item_list.append({'name1':name, 'content':content})

    # 将每条评论返回
    return item_list


if __name__ == "__main__":

    # 所有数据
    allData = []
    # [{name1:zh, content:22},{name1:zh, content:22},{name1:zh, content:22},{name1:zh, content:22},...]

    # 遍历每一页的数据
    for i in range(1, 4):
        url = "https://www.qiushibaike.com/text/page/" + str(i) + "/"
        list1 = getData(url)
        allData.extend(list1)

        time.sleep(0.5)


    # 遍历allData 把数据显示
    for dict1 in allData:
        print("%s 说： %s" % (dict1["name1"], dict1["content"]))




