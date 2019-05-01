import requests
headers = {
 "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
}
#获取接口
url = "http://www.renren.com/PLogin.do"
data = {
    'email':"gaohj5@163.com",
    'password':'12qwaszx',
}

sessions = requests.session()
response = sessions.post(url,data=data,headers=headers)

print(response.text)