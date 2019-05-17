import requests

#GET 请求
responses =requests.get('http://www.qfedu.com/')
# print(responses)#<Response [200]>
# print(responses.status_code)#200
# print(responses.url)#http://www.baidu.com
# print(responses.encoding)#编码
# print(responses.cookies)#cookie
# print(responses.text) #字符串
# print(type(responses.text))
# print(responses.content)#响应数据 二进制
# print("*"*20)
# print(responses.content.decode())

headers = {
   "User-Agent":"User-Agent, Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"
}

params = {
    'wd':"岛国教育片"
}

response = requests.get("http://www.baidu.com/s",params=params,headers=headers)
# print(response.content.decode())
print(response.status_code)


