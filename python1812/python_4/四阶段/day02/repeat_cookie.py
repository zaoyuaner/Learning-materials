import urllib.request
from http import cookiejar


#创建cookiejar对象 跟文件交互 一般用LWPCookieJar
cookie = cookiejar.LWPCookieJar()

#加载本地的cookie
cookie.load(filename="baidu.txt")
#创建cookie 处理器
handler = urllib.request.HTTPCookieProcessor(cookie)

#创建打开器
opener= urllib.request.build_opener(handler)

headers = {
    "User-Agent":"User-Agent, Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"
}

url = "http://www.baidu.com/"
req = urllib.request.Request(url=url,headers=headers)

response = opener.open(req)
print(response.read().decode('utf-8'))