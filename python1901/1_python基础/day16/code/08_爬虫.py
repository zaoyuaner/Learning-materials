#
# 爬虫: 蜘蛛Spider
#

# requests
import requests
import re

# pip 第三方包管理
#   pip install requests  安装包
#   pip uninstall requests 卸载包
#   pip freeze  显示自己安装的包
#   pip list  显示所有包
#   pip -V  查看版本
#   pip show requests 查看包详情

url = 'https://search.51job.com/list/040000,000000,0000,00,9,99,python,2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='
res = requests.get(url)
string = res.content.decode('gbk')
# print(string)

pattern = '<div class="rt">(.*?)</div>'
res = re.findall(pattern, string, re.S)
# print(res)m
string2 = res[0]
# print(string2)

# 取数字
# string2 = string2.strip()
# print(string2)
res2 = re.findall('(\d+)', string2)
print(res2)
print(res2[0])














