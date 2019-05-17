import random
import urllib.request
headers = {
    "User-Agent":"User-Agent, Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"
}

proxy = {'http':'http://user1:123456@10.20.152.204:808'}
# ip_list = [
# {'http':'http://116.209.53.191:9999'},
# {'https':'https://221.218.102.146:33323'},
# {'http':'http://183.148.157.128:9999'},
# ]

ua_list = [
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)",
    "Mozilla/5.0 (iPod; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5"
]

#proxy = random.choice(ip_list)
#设置代理
proxy_handler = urllib.request.ProxyHandler(proxies=proxy)

#创建打开服务器
opener = urllib.request.build_opener(proxy_handler)

url = "http://www.qfedu.com/"
req= urllib.request.Request(url,headers=headers)
req.add_header('User-Agent',random.choice(ua_list))
#print(req.get_header('User-agent'))
response = opener.open(req) #使用代理
print(response.read())