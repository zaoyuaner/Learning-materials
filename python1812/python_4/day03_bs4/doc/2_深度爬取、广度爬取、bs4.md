## 深度爬取、广度爬取、bs4  

## 复习  

```
handler = handler #创建处理器    HttpHandler /HttpsHandler
opener = build_opener(处理器对象)

opener.open()

from http import cookiejar 
1.创建cookies 对象 用来管理cookie CookieJar
2.cookie处理器 = urllib.request.HTTPCookieProcessor(cookies对象)
3.opener= build_opener（cookie处理器 ） #创建打开器


#使用代理   
proxy_list = [
    {'http':"http://ip地址：端口号"}
    
 ]
proxy = random.choice(proxy_list)
proxy_handler = urllib.request.ProxyHandler(proxies=proxy) #创建代理处理器 



requests  pip install requests 

底层其实就是urllib3  
http://www.baidu.com/?wd=kangbazi 
get requests.get(url,params=params,headers=headers)
post



```

## requests.session 模拟登陆并获取 

```
笔趣阁 

import requests
headers = {
 "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
}
#获取接口
url = "http://www.xbiquge.la/login.php"

data = {
    "LoginForm[username]":"kangbazi6",
    "LoginForm[password]":"123123"
}

sessions = requests.session()
response = sessions.post(url,data=data,headers=headers)
print(response.text)

print("++++登陆之后"*10)
url1 = "http://www.xbiquge.la/modules/article/bookcase.php"

response1 = sessions.post(url1,headers=headers)
print(response1.text)


人人网   

import requests
headers = {
 "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
}
#获取接口
url = "http://www.renren.com/ajaxLogin/login?1=1&uniqueTimestamp=20193398742"

data = {
    "email": "gaohj5@163.com",
    "icode": "",#输入验证码
    "origURL": "http://www.renren.com/home",
    "domain": "renren.com",
    "key_id": 1,
    "captcha_type": "web_login",
    "password": "671d3f5a688f39b3e5c66bf7ac3c8139413424522edb1a329b2618048f3adb27",
    "rkey": "41b44b0d062d3ca23119bc8b58983104",
    "f": ""
}

sessions = requests.session()
response = sessions.post(url,data=data,headers=headers)
print(response.text)

url = "http://www.renren.com/541197383/profile"
response2 = sessions.get(url,headers=headers)

print(response2.text)
```



## 深度爬取策略  

> 如果一个页面中还有url  下一级还有url ... 一级一级往下往下抓  

```
# 获取页面的子列表  首先先获取内容
#然后匹配出a标签中的href

import re
import requests
headers = {
 "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
}
#获取网页内容
def get_content(url):
    try:
        res = requests.get(url,headers=headers)
        return res.text
    except:
        return ""
#获取子url列表
def get_son_url(url):
     contentes = get_content(url) #页面的内容
     href_re = '<a.*?href="(.*?)".*?>'
     href_list = re.findall(href_re,contentes,re.S)
     return href_list
def deep_crawer(url):

    if deep_dict[url]>3:
        return
    print("+"*20)
    print("\t"*deep_dict[url],"当前层级:%d" %deep_dict[url])
    son_list = get_son_url(url)
    for sonurl in son_list:
        #列表中http开头的就是有效的
        if sonurl.startswith('http'):
            #去重
            if sonurl not in deep_dict:
                #子url的层级就是父url的层级+1
                deep_dict[sonurl] = deep_dict[url] + 1
                deep_crawer(sonurl)

if __name__ == "__main__":
    url = "https://www.baidu.com/s?wd=岛国教育片"

    #将key 存放 url value存放层级 1 2 3
    deep_dict={} #这里边存放我们所有的列表
    deep_dict[url] = 1
    #开始爬取
    deep_crawer(url)
```



## 广度爬取   宽度优先遍历 也叫广度遍历  

>  抓取起始页面 所有的链接  然后选择其中的一个链接 继续抓这个链接中的所有网页   具体查看 广度优先爬取策略.png    

```
# #doc homework test
# #homework test stu
#  test stu vedio

import re
import requests
headers = {
 "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
}

#获取网页内容
def get_content(url):
    try:
        res = requests.get(url,headers=headers)
        return res.text
    except:
        return ""

#获取子url列表
def get_son_url(url):
     contentes = get_content(url) #页面的内容
     href_re = '<a.*?href="(.*?)".*?>'
     href_list = re.findall(href_re,contentes,re.S)
     return href_list

def width_crawer(start_url):
    #队列模拟
    #入队列 append() 出队列pop()
    url_quene = []
    url_quene.append(start_url)
    while len(url_quene) > 0:
        url = url_quene.pop(0)
        print("\t" * deep_dict[url], "当前层级:%d" % deep_dict[url])
        if deep_dict[url] <= 3:
            #获取子url列表
            sonurl_list = get_son_url(url)
            for sonurl in sonurl_list:
                #过滤有效的链接
                if sonurl.startswith('http'):
                    #去重 为了不重复爬取
                    if sonurl not in deep_dict:
                        deep_dict[sonurl] = deep_dict[url]+1
                        url_quene.append(sonurl)



if __name__ == "__main__":
    url = "https://www.baidu.com/s?wd=苍老师"

    #将key 存放 url value存放层级 1 2 3
    deep_dict={} #这里边存放我们所有的列表
    deep_dict[url] = 1
    #开始爬取
    width_crawer(url)
```

