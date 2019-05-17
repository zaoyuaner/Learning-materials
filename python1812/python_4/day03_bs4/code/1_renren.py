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