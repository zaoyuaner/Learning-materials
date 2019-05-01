'''
    正则表达式 (Regular Expression)
    作用：匹配指定规则的字符串

'''

# 验证手机号：11位，第一位必需是1
# def fn(phone):
#     if len(phone) != 11:
#         return False
#     if phone[0] != '1':
#         return False
#     if not phone.isdigit():
#         return False
#     return True
#
# print(fn('13899998888'))


# 正则表达式
# 使用正则的方法
# re.match()
# re.search()
# re.findall()

import re
# re.match(): 开头匹配，类似str.startswith()
#   flags :
#       re.I : 忽略大小写
#       re.S : 和符号.搭配使用，让.可以匹配到换行符\n
#       re.M : 换行模式
res = re.match('www', 'www.baidu.com')
res = re.match('www', 'baidu.www.com')  # None
res = re.match('www', 'wwwww.baidu.wwwww.com')
res = re.match('www', 'WWw.baidu.com')  # None, 区分大小写
res = re.match('www', 'WWw.baidu.com', re.I)  #
# print(res)

# re.search(): 是否包含正则表达式所匹配的内容
res = re.search('www', 'www.taobao.com')
res = re.search('www', 'taobao.www.com')
res = re.search('www', 'www.taobao.www.com')  # 只找到第一个匹配的内容
res = re.search('www', 'taobao.com')  # None
res = re.search('www', 'WWWWW.taobao.com', re.I)
# print(res)

# re.findall() : 获取所有匹配的内容
res = re.findall('www', 'www.jd.com')  # ['www']
res = re.findall('www', 'www.jd.wwwww.com')  # ['www', 'www']
res = re.findall('www', 'www.jd.wWwWww.com', re.I)  # ['www', 'wWw', 'Www']
res = re.findall('www', 'jd.com')  # []
print(res)


