# -*- coding:utf-8 -*-
import  urllib2

url = 'http://www.baidu.com/'
#urlopen需要三个参数
#url 你要抓取的url
#data 默认为None 为none说明get 请求  如果你data不为none 就认为是post请求
#timeout 超时时间
res = urllib2.urlopen(url, data=None)
#print res
#print res.read() #返回所有的内容
#print res.readline() #按照行返回
#print res.readlines() #返回所有的行
#print res.getcode() #获取客户端请求的状态
#print res.geturl() #获取请求的url
#print res.code
print res.read().decode('utf-8')
#encode
