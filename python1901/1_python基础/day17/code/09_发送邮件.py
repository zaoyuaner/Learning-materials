import smtplib
from email.mime.text import MIMEText  # 创建邮件

# 邮箱，邮件

# smtp服务器：smtp.163.com
# 端口： 25
# 邮箱账号：niejeff@163.com
# 授权码：123456abcde


smtp_server = 'smtp.163.com'
smtp_port = 25
from_email = 'm19976710924@163.com'
auth_code = '123abc'

to_email = '1317502355@qq.com'

# 创建邮箱对象
smtp = smtplib.SMTP(smtp_server, smtp_port)
smtp.login(from_email, auth_code)

# 创建邮件
msg = MIMEText('你还记得那年你在我家楼下站了一宿没睡吗')
msg['Subject'] = '阁下萌萌'
msg['From'] = from_email
msg['To'] = to_email

# 发送
smtp.sendmail(from_email, to_email, msg.as_string())

# 关闭
smtp.close()






