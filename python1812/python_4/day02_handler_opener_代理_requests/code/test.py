import urllib.request
import http.cookiejar
import urllib.parse

#创建 cookiehar对象

cookie = http.cookiejar.CookieJar()
#创建处理器对象
handler = urllib.request.HTTPCookieProcessor(cookie)

#根据处理器对象 创建打开对象
opener = urllib.request.build_opener(handler)
url = "你的weibo url "
headers = {
	'Host': 'weibo.com',
	'Connection': 'keep-alive',
	'Upgrade-Insecure-Requests': '1',
	'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36',
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
	'Referer': 'Referer: https://weibo.com/719755123/home?wvr=5',
	# 'Accept-Encoding': 'gzip, deflate, br',
	'Accept-Language': 'zh-CN,zh;q=0.9',
	'Cookie': 'SINAGLOBAL=712904372122.92.1530759954120; un=2287228249@qq.com; UOR=www.internetke.com,widget.weibo.com,login.sina.com.cn; wb_view_log=1440*9001; YF-V5-G0=aac25801fada32565f5c5e59c7bd227b; Ugrow-G0=e66b2e50a7e7f417f6cc12eec600f517; wb_view_log_2294484062=1440*9001; _s_tentry=-; Apache=9058180744260.998.1554185829872; ULV=1554185830150:4:3:3:9058180744260.998.1554185829872:1554135800194; login_sid_t=35dbb08234bf0ccd0ce7b63bfe9b432d; cross_origin_proto=SSL; WBStorage=201904021417|undefined; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WW--2vNCsOjWn6djugwy4Kj5JpX5K2hUgL.FozE1KBX1hB7Soz2dJLoI79rqgvQIo-t; ALF=1585721871; SSOLoginState=1554185872; SCF=Au5Nqv3Xq1fKc8xIHcwoDi6S6MCknrdmWSaCVBPwW3apcisXAvz0TjXVrKTngpHKYUyHgu2Xpzx5sqHjakihps4.; SUB=_2A25xpo7ADeRhGeRM4lYV-CrMzT6IHXVS1ecIrDV8PUNbmtBeLXDQkW9NU9Q8tQEaC_GJ8MrJoOKpMCJulqP1KSKS; SUHB=0XDUfjjnZnS84l; wvr=6; YF-Page-G0=c704b1074605efc315869695a91e5996|1554186028|1554185822; webim_unReadCount=%7B%22time%22%3A1554186063947%2C%22dm_pub_total%22%3A0%2C%22chat_group_pc%22%3A0%2C%22allcountNum%22%3A27%2C%22msgbox%22%3A0%7D'
}
req = urllib.request.Request(url=url,headers=headers)
#发送请求

response = opener.open(req)
#print(response.read().decode('utf-8'))
with open('weibo.html','wb') as fp:
	fp.write(response.read())
