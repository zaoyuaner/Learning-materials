# -*- coding:utf-8 -*-
import os
import urllib
import urllib2

# urllib 和 urllib2 的区别:
#urllib仅仅接收url  能用urlencode 进行编码  urllib.urlencode()
#urllib2 可以接收设置了 headers 的 Request类
#以上 就让我们经常两个搭配来使用

#https://www.baidu.com/s?wd=美女
def baidu_search(params):

    headers = {
        "User-Agent":"User-Agent, Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"
    }

    url = "http://www.baidu.com/s?"+params

    requests = urllib2.Request(url,headers=headers)
    #print requests
    response = urllib2.urlopen(requests)
    #print response
    print response.read()

    dir = './'
    os.chdir(dir)
    file = urllib2.urlopen(url).read()
    open('baidu.html',"wb").write(file)
    print "OK"
if __name__ == "__main__":
    kw = raw_input("请输入要查找的内容")
    params = {
        'wd':kw
    }
    params = urllib.urlencode(params)
    baidu_search(params)


