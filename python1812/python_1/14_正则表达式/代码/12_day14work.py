import re
# 中文
chinesePattern = "[\u4e00-\u9fa5]+"

# 匹配手机号
if re.match(r"1(1|3|5|7|8|9|4)\d{9}$","18476991120"):
	print("ok")
else:
	print("no")

# 匹配qq号： 5-11位, 第一位不能为0
if re.match(r"[1-9]\d{4,10}$","1072368564"):
	print("ok")
else:
	print("no")
# 匹配任意一个邮箱   如：jack@163.com


# 匹配身份证
result = re.match(r"\d{6}(19\d{2}|20(0|1)\d)(0[1-9]|1[012])(0[1-9]|(1\d|2\d)|3[01])\d{3}[0-9Xx]$","420923199410072510")
print(result)

# 邮政编码(共6位数字, 第一位不能为0)

# 用户名(只能使用数字字母下划线, 且数字不能开头, 长度在6-15位)

# 简单日期格式 如："2017-11-11"，"2017-1-1"

# 图片文件格式 如："nbb.jpg", "aa.jpeg","aa.png", "aa.gif"
result = re.match(r"\w+\.(jpg|jpeg|png|gif)","1.jpg",re.I)      # 不区分大小写
print(result)

# 匹配网址
# 1,匹配下列url网址
# http://www.baidu.com
# https://org.baidu.net
# https://www.sina.com.cn
reg = "https?://(\w+\.)+\w+"
if re.match(r"(http|https)://(\w+\.)+(com|net|cn)$","http://www.baidu.com",re.I):
	print("ok")

# 2,匹配1和下列url网址
# https://www.baidu.com/index.html
# https://www.baidu.com:8080/aaa/bbb/index.asp     # :8080 端口  0-65535
# https://www.baidu.com:80/ccc/ddd/login.html
result = re.match(r"(http|https)://(\w+\.)+(com|net|cn)(:\d{1,5})?(/?\w*)*(\.\w+)*$","http://www.baidu.com:880/aa/bb/index.html",re.I)
if result:
	print("匹配",result)

# 3,匹配1和2以及下列带参数的url网址    # 参数必须以?开头
# http://www.sina.cn:80/index.html?username=goudan
# https://org.baidu.com/login.asp?username=goudan&passwd=222
# https://www.sina.cn:8080/aaa/bbb/index.html?username=goudan&passwd=222&age=333

result = re.match(r"(http|https)://(\w+\.)+(com|net|cn)(:\d{1,5})?(/?\w*)*(\.\w+)*(\??\w+=\w+&?)*$","http://www.baidu.com:880/aa/bb/index.html?username=goudan",re.I)
if result:
	print("匹配",result,len("http://www.baidu.com:880/aa/bb/index.html?username=goudan"))
