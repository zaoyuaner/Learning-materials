import urllib.request
http = urllib.request.HTTPHandler(debuglevel=1)#z这个是支持http的
#https = urllib.request.HTTPSHandler()#z这个是支持http的

#调用方法使用这个对象   创建打开器对象
opener = urllib.request.build_opener(http)
headers = {
    "Cookie":"pgv_pvid=5146724799; AMCV_248F210755B762187F000101%40AdobeOrg=-1891778711%7CMCIDTS%7C17761%7CMCMID%7C71991122967003593260888412583202511071%7CMCAAMLH-1535104600%7C11%7CMCAAMB-1535104600%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1534507000s%7CNONE%7CMCAID%7CNONE%7CMCSYNCSOP%7C411-17768%7CvVersion%7C2.4.0; pgv_pvi=6441753600; RK=iORgFZkhkT; ptcz=50a7d664f0d2587d5cf3524469b873afbeef308c52bf29456c46be6ead1c1b7a; o_cookie=2287228249; ptui_loginuin=2287228249; qz_screen=1440x900; QZ_FE_WEBP_SUPPORT=1; cpu_performance_v8=6; __Q_w_s__QZN_TodoMsgCnt=1; pgv_si=s3102401536; _qpsvr_localtk=0.8959738178804983; ptisp=ctc; pgv_info=ssid=s7595278691; uin=o2287228249; skey=@xIp1fyofJ; p_uin=o2287228249; pt4_token=ck7T7G10Qf7TV-eMDd-pnC1OP5R6XGKeM0UpqAJfxV4_; p_skey=U4BbP1qlJgmXueZ6gQjjrVeZ3XJ*cWdLUlw*eLdg3vA_; Loading=Yes; x-stgw-ssl-info=36feb41d19b5baab0be6eced113003b3|0.102|1554174772.492|1|.|Y|TLSv1.2|ECDHE-RSA-AES128-GCM-SHA256|14000|h2|0",
    "User-Agent":"User-Agent, Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"
}

url = "https://user.qzone.qq.com/2287228249"

req = urllib.request.Request(url,headers=headers)
response = opener.open(req)

print(response.read().decode())