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