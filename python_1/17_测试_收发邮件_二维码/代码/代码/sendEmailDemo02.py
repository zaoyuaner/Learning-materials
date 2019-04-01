#发送带有附件的邮件

import  smtplib
from  email.mime.text import MIMEText
from  email.mime.multipart import MIMEMultipart   #附件
from  email.mime.application import MIMEApplication

username = "18501970795@163.com"
password = "yang0122"
sender = username
recevier = ",".join(["1490980468@qq.com"])

#创建一个关于附件的对象
msg = MIMEMultipart()
msg["From"] = sender
msg["To"] = recevier
msg["Subject"] = "带有附件的邮件"

#创建一个关于正文的对象
text = MIMEText("today is a good day")

#将附件和文本做整合
msg.attach(text)

#设置附件部分
file = open("dog.jpg","rb")
imagePart = MIMEApplication(file.read())
#设置图片的相关信息
imagePart.add_header("Content-Disposition","attachment",filename="dog.jpg")
msg.attach(imagePart)

smtpObj = smtplib.SMTP()
smtpObj.connect("smtp.163.com")
smtpObj.login(username,password)
smtpObj.sendmail(sender,recevier,msg.as_string())

#退出服务器
smtpObj.quit()





