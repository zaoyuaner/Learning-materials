import requests
headers = {
   "User-Agent":"User-Agent, Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"
}

proxy = {'http':'http://user1:123456@10.20.152.204:808'}

url="http://www.baidu.com/"
response = requests.get(url,headers=headers,proxies=proxy)
print(response.text)