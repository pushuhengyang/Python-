
'''发送邮件'''

import  smtplib
from email.mime.text import MIMEText
from email.header import Header

# 网易 smtp.163.com  465/994   25
mail_host = 'smtp.163.com'
mail_user = "wenhao201000@163.com"
mail_pass = 'feng4057'

sender   = mail_user
receive  = '601778466@qq.com'

# 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
mess = MIMEText('python c测试','plain','utf-8')
mess['From'] = sender
mess['To']   = receive

subject = 'Python  第一封邮件'
mess['Subject'] = Header(subject,'utf-8')

try:
    smtobj = smtplib.SMTP()
    smtobj.connect(mail_host,25)
    smtobj.login(mail_user,mail_pass)
    smtobj.sendmail(sender,receive,mess.as_string())
    print('发送成功')
except smtplib.SMTPException:
    print('发送失败')
