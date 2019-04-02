import urllib.request

#创建处理器对象

http = urllib.request.HTTPHandler(debuglevel=1)#z这个是支持http的
#https = urllib.request.HTTPSHandler()#z这个是支持http的

#调用方法使用这个对象   创建打开器对象
opener = urllib.request.build_opener(http)

#打开url
# response = opener.open("http://www.baidu.com/")
# # print(response.read().decode())
#创建 全局打开器

urllib.request.install_opener(opener) #使用了全局打开器  后面的urlopen 也会使用
response = urllib.request.urlopen("http://www.ifeng.com/")
#print(response.read().decode())