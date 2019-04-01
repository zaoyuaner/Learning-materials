import smtplib
from email.header import Header
from email.mime.text import MIMEText

class Emailer:
	def __init__(self,username,password,host):    # password 授权码
		self.username = username
		self.password = password
		self.host = host           # smtp服务器地址

	def sendMail(self,sender,receiver,content,title):
		"""

		:param sender:  发送者
		:param receiver:  接受者
		:param content:  邮件内容
		:param title:  邮件标题
		:return:
		"""
		# 第一步发送准备
		# 参数: 邮件内容, 格式和编码
		message = MIMEText(content,'plain','utf-8')
		message["From"] = sender        # 发送者
		message['To']   = receiver       # 接收者
		message['Subject'] = title

		# 第二部分: 发送
		try:
			# 邮件服务器地址, 端口
			smtpObject = smtplib.SMTP(self.host,25)
			# 登录邮箱
			# 参数: 用户名  ,授权码
			smtpObject.login(self.username,self.password)
			# 发送邮件
			# 参数: 发送者, 接收者, 邮件内容
			smtpObject.sendmail(sender,receiver,message.as_string())# as_string  变字符串
			print("发送成功")
		except Exception as e:
			print(e)

if __name__ == "__main__":
	username = "zxcyzk0911@163.com"
	password = "yzk911"
	host = "smtp.163.com"
	emaill = Emailer(username,password,host)
	emaill.sendMail("zxcyzk0911@163.com","1072368564@qq.com","（python测试邮件) 垃圾,我玩亚索!\n 发送至pycharm编译器","打游戏啊")
