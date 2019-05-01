
# 中文
chinesePattern = "[\u4e00-\u9fa5]+"


# 匹配手机号


# 匹配qq号： 5-11位, 第一位不能为0

# 匹配任意一个邮箱   如：jack@163.com，11@qq.com, aaa@sina.com.cn

# 匹配身份证: 18位，最后一位可能是X

# 邮政编码(共6位数字, 第一位不能为0)

# 用户名(只能使用数字字母下划线, 且数字不能开头, 长度在6-15位)

# 简单日期格式 如："2017-11-11"，"2017-1-1"

# 图片文件格式 如："nbb.jpg", "aa.jpeg","aa.png", "aa.gif"


# 匹配网址
# 1,匹配下列url网址
# http://www.baidu.com
# https://org.baidu.net
# https://www.sina.com.cn
reg = "https?://(\w+\.)+\w+"


# 2,匹配1和下列url网址
# https://www.baidu.com/index.html
# https://www.baidu.com:8080/aaa/bbb/index.asp
# https://www.baidu.com:80/ccc/ddd/login.html


# 3,匹配1和2以及下列带参数的url网址
# http://www.sina.cn:80/index.html?username=goudan
# https://org.baidu.com/login.asp?username=goudan&passwd=222
# https://www.sina.cn:8080/aaa/bbb/index.html?username=goudan&passwd=222&age=333





# 扩展：爬取51job的岗位名称和薪资
# url = "https://search.51job.com/list/040000,000000,0000,00,9,99,python,2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare="



