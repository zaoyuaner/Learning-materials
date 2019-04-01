#发送纯文本
#发邮件的模块
import  smtplib
#邮件标题
from  email.header import Header
#邮件文本
from  email.mime.text import MIMEText

"""
user:用户名
pwd:授权码
sender：发送方
receiver：接收方
content：邮件的正文
title：邮件的标题
"""
def sendMail(user,pwd,sender,receiver,content,title):
    mail_host = "smtp.163.com"   #163的SMTP服务器

    #第一部分：准备工作
    #1.将邮件的信息打包成一个对象
    message = MIMEText(content,"plain","utf-8")   #内容，格式，编码
    #2.设置邮件的发送者
    message["From"] = sender
    #3.设置邮件的接收方
    #message["To"] = receiver
    #join():通过字符串调用，参数为一个列表
    message["To"] = ",".join(receiver)
    #4.设置邮件的标题
    message["Subject"] = title

    #第二部分：发送邮件
    #1.启用服务器发送邮件
    #参数：服务器，端口号
    smtpObj = smtplib.SMTP_SSL(mail_host,465)
    #2.登录邮箱进行验证
    #参数：用户名，授权码
    smtpObj.login(user,pwd)
    #3.发送邮件
    #参数：发送方，接收方，邮件信息
    smtpObj.sendmail(sender,receiver,message.as_string())

    print("mail send successful!")

if __name__ == "__main__":
    mail_user = "18501970795@163.com"
    mail_pwd = "yang0122"

    mail_sender = "18501970795@163.com"
    mail_receiver = ["1490980468@qq.com"]

    email_content = "人生苦短，我用Python"
    email_title = "Python1805"

    sendMail(mail_user,mail_pwd,mail_sender,mail_receiver,email_content,email_title)
