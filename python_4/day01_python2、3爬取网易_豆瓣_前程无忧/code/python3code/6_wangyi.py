import json
import urllib.request
import urllib.parse

headers = {
"User-Agent":"User-Agent, Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"
}
url = 'https://music.163.com/weapi/v1/resource/comments/A_PL_0_2386637465?csrf_token='
data = {
    "params": "IMMh0aWzreEhrbqaIjYKCkSvKIarMpJsMTcQ92b4lDOnlOZ6bNlkE/rAPDWDjIIOcdLHuLvuWk6tOvAe8r0JU93bUs1peT2w5Zc1zoiUVTAXXJaJOI9ZUp02VLLA/aqPh3ugCeE9T/oXYMknnASO25t8lhFcRpM3TAPArQsYhYqBCp0lBsifqnxktlMfN8jhBwXXxJzq2v2dtXIb9K7oMLeySbFgz4Rx+sC3olkP4fQ=",
    "encSecKey": "0afc0ae61575480fd9bc168ef82df0d0ed2c699657f91000baf019f14600d19882d1334bb2f5703c658f6300c57935bd8278183765a5aeaa773c25673b24a125584cefee6d30cebc6fb3f40891a8e047b1626e091dfaf0279de90104af64eec23411f560d14278fe69b28bb292a883b58747ae5a03357ea243d3832f1c64b9a6"
}
#将post请求传入二进制参数
data = urllib.parse.urlencode(data).encode()
#print(data)
#创建请求对象 加上data 就变成了post请求
req = urllib.request.Request(url,headers=headers,data=data)
#获取返回数据
response = urllib.request.urlopen(req)
content = response.read().decode()
print(content)

comments_list = json.loads(content)
host_comments = comments_list['hotComments']
for contents in  host_comments:
    nickname = contents['user']['nickname']
    content = contents['content']
    print(nickname,":",content)



