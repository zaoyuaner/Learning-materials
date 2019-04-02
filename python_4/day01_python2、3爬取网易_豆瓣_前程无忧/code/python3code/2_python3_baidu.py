from urllib import request
import urllib.parse
headers = {
"User-Agent":"User-Agent, Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"
}
#/s?wd=
kw = input("请输入关键字:")
params = {
    'wd':kw
}

#将字典解析成参数字符串
params=urllib.parse.urlencode(params)
print(params)

#创建url
url = 'http://www.baidu.com/s?'+params

#创建请求对象
requests= urllib.request.Request(url,headers=headers)
responses = urllib.request.urlopen(requests)

#print(responses.read().decode('utf-8'))
#print(responses.status)
print(responses.__dict__)