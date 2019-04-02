import urllib
from urllib import request

headers = {
"User-Agent":"User-Agent, Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"
}

#url
url = "http://www.baidu.com/"

#创建请求对象
req =urllib.request.Request(url,headers=headers)
#发送请求 获取响应
responses = urllib.request.urlopen(req)
#print(responses)#二进制
# print("*"*30)
# print(responses.read())
# print("*"*30)
print(responses.read().decode('utf-8'))#解码
#字符串->字节   encode
#字节-> 字符串   decode