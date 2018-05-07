
# 发送纯文本
# SMTP: 邮件传输协议

# 发邮件
import smtplib
# 邮件标题
from email.header import Header
# 邮件正文
from email.mime.text import MIMEText

"""
user, pwd, sender, receiver, content, title
用户名，授权码，发送方邮箱，接收方邮箱，内容，标题
"""


def sendEmail(user, pwd, sender, receiver, content, title):
    # 163的SMTP服务器
    mail_host = "smtp.163.com"

    # 第一部分：准备工作
    # 1. 将对应的邮件信息打包成一个对象: 内容， 格式， 编码
    message = MIMEText(content, "plain", "utf-8")
    message["Content-Type"] = 'application/octet-stream'
    message["Content-Disposition"] = 'attachment;filename='+ file
    # 2. 设置邮件的发送者
    message["From"] = sender
    # 3. 设置邮件的接收方
    """
    seq.join(sep)
    seq: 分隔符
    sep: 要连接的元素序列，字符串，元组，字典
    返回值：字符串
    """
    message["To"] = ",".join(receiver)
    # 4. 设置邮件标题
    message["Subject"] = title

    try:
        # 第二部分：发送邮件
        # 1. 启用SSL发送邮件，参数1： SMTP服务器， 参数2 ： 端口号么一般使用465
        smtpObj = smtplib.SMTP_SSL(mail_host, 465)
        # 2.登录邮箱并进行验证
        # 参数1: 发送方用户名，参数2：授权码
        smtpObj.login(user, pwd)
        # 3. 发送邮件
        # 参数1：发送方邮箱 参数2： 接收方的邮箱 参数3：邮件正文
        smtpObj.sendmail(sender, receiver, message.as_string())

        print("mail has been send successful!")
    except BaseException as e:
        print(e)


if __name__ == '__main__':
    mail_user = "zst0717123@163.com"
    mail_pwd = "*****"
    sender = "zst0717123@163.com"
    receiver = "@qq.com"
    file = "beautiful_girl.png"
    content = open(file=file,mode='rb').read()
    title = "666"

    sendEmail(mail_user, mail_pwd, sender, receiver, content, title)
