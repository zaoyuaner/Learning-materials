# -*- coding:utf-8 -*-

import urllib2

headers = {
    "User-Agent":"User-Agent, Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"
}
#url后边要加上/
url = "http://www.baidu.com/"

#创建请求对象
res = urllib2.Request(url,headers=headers)

print res.get_full_url() #获取完整的url
print res.get_method() #获取请求方法
print res.get_header("User-agent") #获取 浏览器的名称
print res.get_host() #host名称
print res.get_type() #协议名称
res.add_header("Connection","keep-alive") #wang header头中添加请求信息

print res.get_header("Connection")
