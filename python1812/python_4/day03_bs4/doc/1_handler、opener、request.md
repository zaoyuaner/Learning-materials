# handler、opener、request

## 复习  

```
urllib2.urlopen() 
urllib.request.urlopen()  这个不能构建请求头 

res = urllib.request.Request(url,headers=headers)

response = urllib.request.urlopen(res)

print(response.read().decode())
```



##  handler、opener 

```
urllib.request.urlopen()  这个不能构建请求头 
于是引入了 res = urllib.request.Request(url,headers=headers) 构建请求对象    
但是urllib.request.Request 不能携带cookie 而且不能使用代理   所以引入 Handler 处理器 自定义opener对象  

流程:  
1.构建 HttpHandler 对象  支持http https  
	HttpHandler  支持http
	HttpsHandler 支持 https
2.调用 builder_opener() 来使用上面的对象  创建打开对象
3.调用上面对象的open() 来代替之前的 urlopen()


import urllib.request

#创建处理器对象

http = urllib.request.HTTPHandler()#z这个是支持http的
#https = urllib.request.HTTPSHandler()#z这个是支持http的

#调用方法使用这个对象   创建打开器对象
opener = urllib.request.build_opener(http)

#打开url
# response = opener.open("http://www.baidu.com/")
# # print(response.read().decode())
#创建 全局打开器

urllib.request.install_opener(opener) #使用了全局打开器  后面的urlopen 也会使用 
response = urllib.request.urlopen("http://www.ifeng.com/")
print(response.read().decode())



在处理器HTTPHandler、HTTPSHandler里边加上debuglevel=1 会开启 debug log日志   会在终端打印 受包发包的header 头  这样会省去抓包的操作  
```



## Cookie 本身就是文件

```
pv  page view  
uv  user visitor  以cookie 为区分  
```



    Cookie 是指某些网站服务器为了辨别用户身份和进行Session跟踪，而储存在用户浏览器上的文本文件，Cookie可以保持登录信息到用户下次与服务器的会话。
    
    Cookie原理
    
    HTTP是无状态的协议, 为了保持连接状态, 引入了Cookie机制 Cookie是http消息头中的一种属性，包括：
    Cookie名字（Name）
    Cookie的值（Value）
    Cookie的过期时间（Expires/Max-Age）
    Cookie作用路径（Path）
    Cookie所在域名（Domain），
    使用Cookie进行安全连接（Secure）。
    
    前两个参数是Cookie应用的必要条件，另外，还包括Cookie大小（Size，不同浏览器对Cookie个数及大小限制是有差异的）。cookie最大不超过4k  
    
    Cookie由变量名和值组成，根据 Netscape公司的规定，Cookie格式如下：
    Set－Cookie: NAME=VALUE；Expires=DATE；Path=PATH；Domain=DOMAIN_NAME；SECURE

## Cookie应用



    Cookies在爬虫方面最典型的应用是判定注册用户是否已经登录网站，用户可能会得到提示，是否在下一次进入此网站时保留用户信息以便简化登录手续。 爬取信息的过程中 绕过登陆 
    
    cookielib库 和 HTTPCookieProcessor处理器
    在Python处理Cookie，一般是通过cookielib模块和 urllib2模块的HTTPCookieProcessor处理器类一起使用。
    
    cookielib模块：主要作用是提供用于       存储cookie的对象
    
    HTTPCookieProcessor处理器：主要作用是处理这些cookie对象，并构建handler对象。
    
    cookielib 库
    	该模块主要的对象有CookieJar、FileCookieJar、MozillaCookieJar、LWPCookieJar。
    
    CookieJar：管理HTTP cookie值、存储HTTP请求生成的cookie、向传出的HTTP请求添加cookie的对象。整个cookie都存储在内存中，对CookieJar实例进行垃圾回收后cookie也将丢失。
    
    FileCookieJar (filename,delayload=None,policy=None)：从CookieJar派生而来，用来创建FileCookieJar实例，检索cookie信息并将cookie存储到文件中。filename是存储cookie的文件名。delayload为True时支持延迟访问访问文件，即只有在需要时才读取文件或在文件中存储数据。
    
    MozillaCookieJar (filename,delayload=None,policy=None)：从FileCookieJar派生而来，创建与Mozilla浏览器 cookies.txt兼容的FileCookieJar实例。
    
    LWPCookieJar (filename,delayload=None,policy=None)：从FileCookieJar派生而来，创建与libwww-perl标准的 Set-Cookie3 文件格式兼容的FileCookieJar实例。
    
    其实大多数情况下，我们只用CookieJar()，如果需要和本地文件交互，就用 MozillaCookjar() 或 LWPCookieJar()


## 模拟登陆 qq空间  

```
import urllib.request
http = urllib.request.HTTPHandler(debuglevel=1)#z这个是支持http的
#https = urllib.request.HTTPSHandler()#z这个是支持http的

#调用方法使用这个对象   创建打开器对象
opener = urllib.request.build_opener(http)
headers = {
    "Cookie":"pgv_pvid=5146724799; AMCV_248F210755B762187F000101%40AdobeOrg=-1891778711%7CMCIDTS%7C17761%7CMCMID%7C71991122967003593260888412583202511071%7CMCAAMLH-1535104600%7C11%7CMCAAMB-1535104600%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1534507000s%7CNONE%7CMCAID%7CNONE%7CMCSYNCSOP%7C411-17768%7CvVersion%7C2.4.0; pgv_pvi=6441753600; RK=iORgFZkhkT; ptcz=50a7d664f0d2587d5cf3524469b873afbeef308c52bf29456c46be6ead1c1b7a; o_cookie=2287228249; ptui_loginuin=2287228249; qz_screen=1440x900; QZ_FE_WEBP_SUPPORT=1; cpu_performance_v8=6; __Q_w_s__QZN_TodoMsgCnt=1; pgv_si=s3102401536; _qpsvr_localtk=0.8959738178804983; ptisp=ctc; pgv_info=ssid=s7595278691; uin=o2287228249; skey=@xIp1fyofJ; p_uin=o2287228249; pt4_token=ck7T7G10Qf7TV-eMDd-pnC1OP5R6XGKeM0UpqAJfxV4_; p_skey=U4BbP1qlJgmXueZ6gQjjrVeZ3XJ*cWdLUlw*eLdg3vA_; Loading=Yes; x-stgw-ssl-info=36feb41d19b5baab0be6eced113003b3|0.102|1554174772.492|1|.|Y|TLSv1.2|ECDHE-RSA-AES128-GCM-SHA256|14000|h2|0",
    "User-Agent":"User-Agent, Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"
}

url = "https://user.qzone.qq.com/2287228249"

req = urllib.request.Request(url,headers=headers)
response = opener.open(req)

print(response.read().decode())
```

## 模拟weibo.cn登陆  

```
import urllib.request
import http.cookiejar
import urllib.parse

#创建 cookiejar对象

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
```



## 练习  模拟登陆人人网   

```
http://www.renren.com/ajaxLogin/login?1=1&uniqueTimestamp=2019321457754

data = {
    captcha_type
    username
    password
    ....
}

opener.open(req)

url = "个人主页的时候 "
opener.open(req) 这里保存了我们的cookie信息    

打印我们的页面内容 
```

## 下载 cookie  

```
import urllib.request
from http import cookiejar

#创建文件 保存cookie
filename = "baidu.txt"
#创建cookiejar对象 跟文件交互 一般用LWPCookieJar
cookie = cookiejar.LWPCookieJar(filename=filename)
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
print(response)
print(cookie)
cookie.save()
```



## 加载本地cookie

```
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
```





## 反反爬策略 2   proxyhandler   代理设置  

> 免费的代理 
>
>  西刺  
>
> 快代理 
>
> proxy360
>
> 全网代理IP  
>
> 代理云 
>
> 西瓜代理  
>
> 如果代理足够多  可以形成代理池 可以随机选择 choice 

```
import random
import urllib.request
headers = {
    "User-Agent":"User-Agent, Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"
}

proxy = {'http':'http://user1:123456@10.20.152.204:808'} #这个通过 代理客户端设置用户名和密码 
# ip_list = [
# {'http':'http://116.209.53.191:9999'},
# {'https':'https://221.218.102.146:33323'},
# {'http':'http://183.148.157.128:9999'},
# ]

#这个是设置  user_agent 池 
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
```





## requests 库  让http服务人类  

```
requests库继承了 urllib2 所有特性    
支持 http 连接保持  连接池  
支持cookie 会话保持  
支持文件上传 
支持国际化 URL 和POST的编码  

底层就是 urllib3

社区活跃  文档齐全 不可多得  

http://cn.python-requests.org/zh_CN/latest/ 中文文档  
https://github.com/kennethreitz/requests 源码   
```



## 安装  

```
pip install requests 
```

### requests get 

```
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



```

### requests post

```
import requests
import json
headers = {
   "User-Agent":"User-Agent, Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"
}
#translate_o 需要去掉 _o
url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"

english = "frank"
data = {
    "i": english,
    "from": "en",
    "to": "zh-CHS",
    "smartresult": "dict",
    "client": "fanyideskweb",
    "salt": 15541930622862,
    "sign": "f57426a991daf484adf70e8a7d81efca",
    "doctype": "json",
    "version": 2.1,
    "keyfrom": "fanyi.web",
    "action": "FY_BY_REALTlME",
    "typoResult": False,
}

response = requests.post(url,data=data,headers=headers)

# json.load(response.text)
dic = response.json()
print(dic)

tgt = dic['translateResult'][0][0]['tgt']
print(tgt)
```



## requests 操作 cookie 和 session  

```
import requests

headers = {
    "User-Agent":"User-Agent, Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"
}

response = requests.get("http://www.baidu.com/",headers=headers)
print(response.cookies)

#将cookie对象转化成字典

dic = requests.utils.dict_from_cookiejar(response.cookies)
print(dic)
```

## 作业 

* 百度翻译  
* 豆瓣 
* 糗百
* 人人网模拟登陆