import urllib.request
from bs4 import BeautifulSoup

def qq_hr(url):
    headers = {
    "User-Agent":"User-Agent, Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"
    }
    req = urllib.request.Request(url,headers=headers)
    data = urllib.request.urlopen(req).read()
    soup = BeautifulSoup(data,'lxml')

    data = soup.find_all('table',class_="tablelist")
    for line in  data[0].find_all('tr',class_=["even","odd"]):
        for data in line.find_all('td'):
            print(data.string)
qq_hr("https://hr.tencent.com/position.php?keywords=python")