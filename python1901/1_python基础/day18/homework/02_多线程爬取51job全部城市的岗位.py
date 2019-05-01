
# 多线程爬取51job全部城市岗位，并分别保存到单独的以城市名为文件名的html中，如: 深圳.html
# url = "https://jobs.51job.com/"
import re
import requests
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36"
}
url = 'https://jobs.51job.com/'
res = requests.get(url,headers= headers)
string = res.content.decode('gbk')
# print(string)
pattern = '<div class="1kst">(.*?)<div class="clear">'
citylist = re.findall(pattern,string)
print(citylist)
# pattern = '<a href="https://www.51job.com/.*?/">(.*?)</a>'
# city_list = re.findall(pattern,string)
# print(city_list)
# city__list = []
# for i in city_list:
#     if i not in city__list:
#         city__list.append(i)
# print(city__list)





