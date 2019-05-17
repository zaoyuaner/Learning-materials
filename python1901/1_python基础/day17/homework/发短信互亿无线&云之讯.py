
# 互亿无线

#
# 云之讯
import requests

url = r'https://open.ucpaas.com/ol/sms/sendsms'
json = {"sid":"38c7b6c30b8c87ac595acfc5cd650cfc",
        "token":"933daf6df6233e58b78d2cb30c200487",
        "appid":"0872803edebf4955a4fe2a6040bcd493",
        "templateid":"442017",
        "param":"5201314",
        "mobile":"19976710924",
        "uid":""}
res = requests.post(url = url, json = json)
print(res.json())






