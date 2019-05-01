import re
import urllib.request

headers = {
"User-Agent":"User-Agent, Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"
}

#获取前程无忧的接口

url = "https://search.51job.com/list/040000%252C010000,000000,0000,00,9,99,python,2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare="

#抓取数据 创建请求对象
req = urllib.request.Request(url,headers=headers)
#获取服务器响应数据
response = urllib.request.urlopen(req)
# print(response)
#解码
html = response.read().decode('gbk')
# print(html)
#print(type(html))

# 处理数据 拿到标签中间所有的内容
jobnum_re = '<div class="rt">(.*?)</div>'
coms = re.compile(jobnum_re,re.S)
strs = coms.findall(html)[0]
# print(strs)

#贪婪模式  非贪婪模式
#非贪婪模式加上 ？ 变成了 贪婪模式
#取出 纯数字
num_re = '.*?(\d+).*'
num = re.findall(num_re,strs)
# print(num)
# print(int(num[0]))

#获取第一个岗位信息
jobname_re = '<div class="el">(.*?)</div>'
joblist = re.findall(jobname_re,html,re.S)


# #print(joblist[0]) #这是第一个岗位的信息 多个标签
#
# #匹配岗位内容
# jobnameone_re = 'onmousedown="">(.*?)</a>'
# jobnameone_list = re.findall(jobnameone_re,joblist[1],re.S)
# print(jobnameone_list[0].strip())

for job in joblist:
    jobnameone_re = 'onmousedown="">(.*?)</a>'
    jobnameone_list = re.findall(jobnameone_re, job, re.S)
    print(jobnameone_list)
    #print("岗位名称:",jobnameone_list[0].strip())


