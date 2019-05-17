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

response1 = sessions.get(url1,headers=headers,verify=False)#忽略ssl证书
print(response1.text)
