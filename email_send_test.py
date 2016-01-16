#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-01-15
# @Author  : Shoufu (gyming@outlook.com)
# @Version : 2.7.6


# 填好基本信息
from_addr = 'gyming2015@163.com'
password = 'koucuhoezmipgmre'
smtp_server = 'smtp.163.com'
to_addr = '407886535@qq.com'

from email import encoders
from email.mime.text import MIMEText  # ----------- No.1 -----------
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase

text = 'hahahaahahahaha'  # 邮件的内容
# msg = MIMEText(text, 'plain', 'utf-8')  # 构造邮件对象，'plain'指文本，'html'指网页邮件

msg = MIMEMultipart()  # 如果要添加附件，则先构造一个MIMEMultipart对象代表邮件本身
msg.attach(MIMEText(text, 'plain', 'utf-8'))  # 然后往里面加上一个MIMEText作为邮件正文
with open('img/127695.jpg', 'rb') as f:
    mime = MIMEBase('image', 'jpg', filename='abc.jpg')  # 再继续往里面加上表示附件的MIMEBase对象

    # 加上必要的头信息:
    mime.add_header('Content-Disposition', 'attachment', filename='456789.jpg')
    mime.add_header('Content-ID', '<0>')
    mime.add_header('X-Attachment-Id', '0')

    mime.set_payload(f.read())  # 把附件的内容读进来
    encoders.encode_base64(mime)  # 添加到MIMEMultipart
    msg.attach(mime)

from email.header import Header  # ----------- No.2 -----------
from email.utils import parseaddr, formataddr


def _format_addr(string):  # 为了避免邮件地址出现中文，需要对这些地址进行编码
    name, addr = parseaddr(string)
    header_encode = Header(name, 'utf-8').encode()
    addr_encode = addr.encode('utf-8')
    return formataddr((header_encode, addr_encode if isinstance(addr, unicode) else addr))


msg['from'] = _format_addr('发件人大呵呵 <%s>' % from_addr)  # msg['To'] 指的是发件人的地址
msg['to'] = _format_addr('收件人小呵呵 <%s>' % to_addr)  # msg['To']接收的是字符串而不是list，如果有多个邮件地址，用,分隔即可。
msg['subject'] = Header('邮件标题嘿嘿嘿', 'utf-8')  # msg['Subject'] 是邮件的标题，调用Header就可以了

import smtplib  # ----------- No.3 -----------

server = smtplib.SMTP(smtp_server, 25)  # SMTP协议默认端口是25
server.starttls()  # 加密SMTP，即先创建SSL安全连接，然后再使用SMTP协议发送邮件。
server.set_debuglevel(1)  # 可以print出和SMTP服务器交互的所有信息
server.login(from_addr, password)  # 登录SMTP服务器
# 下面是发邮件，由于可以一次发给多个人，所以传入一个list，邮件正文是一个str，as_string()把MIMEText对象变成str。
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()
