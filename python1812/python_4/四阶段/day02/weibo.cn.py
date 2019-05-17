import urllib.request
import http.cookiejar
import urllib.parse

#创建 cookiehar对象

cookie = http.cookiejar.CookieJar()
#创建处理器对象
handler = urllib.request.HTTPCookieProcessor(cookie)

#根据处理器对象 创建打开对象
opener = urllib.request.build_opener(handler)
#这里通过代码 模拟登陆
post_url = "https://passport.weibo.cn/signin/login"

data = {
    "username":"17701256561",
    "password":"lizhibin666",
    "savestate":1,
    "r":"https://weibo.cn/",
    "ec":0,
    "entry":"mweibo",
    "mainpageflag":1,
    "client_id":"",
    "code":"",
    "qq":"",
    "hff":"",
    "hfp":"",
    "wentry":"",
    "loginfrom":"",
    "pagerefer":"",
}
data = urllib.parse.urlencode(data).encode('utf-8')
headers = {
    "Origin": "https://passport.weibo.cn",
    "Accept": "*/*",
    "Content-Type": "application/x-www-form-urlencoded",
    "Connection": "keep-alive",
    "Host": "passport.weibo.cn",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Referer":"https://passport.weibo.cn/signin/login?entry=mweibo&r=https%3A%2F%2Fweibo.cn%2F&backTitle=%CE%A2%B2%A9&vt=",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
}

#构建请求对象
req = urllib.request.Request(url=post_url,headers=headers,data=data)
#发送请求
#这里 opener 保存了登陆之后的cookie 信息
response = opener.open(req)
print(response.read().decode('gb2312'))


url = "https://weibo.cn/6388179289/info"
headers1 = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
}

reqs = urllib.request.Request(url=url,headers=headers1)
#发送请求
#这里 opener 保存了登陆之后的cookie 信息
responses = opener.open(reqs)
#print(responses.read().decode('gb2312'))
