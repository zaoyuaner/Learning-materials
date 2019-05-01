import urllib.request

#第一个参数 要下载的url
#第二个参数  文件存放的路径
#request.urlretrieve("http://www.so.com/",r"baidu.html")

#http://www.baidu.com/?username=中文&password=afdsf

#url中只能写 -_.a-z    如果中文需要转义
urllib.request.urlretrieve("http://p1.so.qhimgs1.com/bdr/576__/t01ff3c9aedf92d7281.jpg",r"苍老师.jpg")


# strings = 'http://www.baidu.com/?username=中文&password=afdsf'
# print(urllib.parse.quote(strings))

strings = 'http%3A//www.baidu.com/%3Fusername%3D%E4%B8%AD%E6%96%87%26password%3Dafdsf'
print(urllib.parse.unquote(strings))