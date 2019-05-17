import requests
from bs4 import BeautifulSoup

headers = {
"User-Agent":"User-Agent, Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"
}

url = "http://quote.stockstar.com/fund/stock.shtml"
#获取数据 requests get方法获取
response = requests.get(url,headers=headers)

#print(response.text)

#处理数据
soup = BeautifulSoup(response.content.decode('gb2312'),'lxml')
tr_list = soup.select('#datalist > tr')
for tr in tr_list:
    # print(tr.text)
    id = tr.select('td')[0].a.text
    name = tr.select('td')[1].a.text
    values = tr.select('td')[2].text
    print(id,name,values)


