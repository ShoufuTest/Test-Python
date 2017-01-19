#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-01-15
# @Author  : Shoufu (gyming@outlook.com)
# @Version : 2.7.6

import os
import os.path

from email import encoders
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.header import Header
from email.utils import parseaddr, formataddr
import smtplib


def attach_file(filename):
    with open(filename, 'rb') as f:
        name = os.path.split(filename)[1]
        file_type = os.path.splitext(filename)[1].replace('.', '')
        mime = MIMEBase('file', file_type, filename=name)
        mime.add_header('Content-Disposition', 'attachment', filename=name)
        mime.add_header('Content-ID', '<0>')
        mime.add_header('X-Attachment-Id', '0')
        mime.set_payload(f.read())
        encoders.encode_base64(mime)
        msg.attach(mime)


def format_addr(string):
    name, addr = parseaddr(string)
    header_encode = Header(name, 'utf-8').encode()
    addr_encode = addr.encode('utf-8')
    return formataddr((header_encode, addr_encode if isinstance(addr, unicode) else addr))

_from_addr = 'gyming2015@163.com'
_password = 'koucuhoezmipgmre'
_smtp_server = 'smtp.163.com'
to_addr = '407886535@qq.com'

text = 'hehe'

msg = MIMEMultipart()
msg.attach(MIMEText(text, 'plain', 'utf-8'))

attach_file('img/git-cheatsheet.pdf')
msg['from'] = format_addr('GYMing <%s>' % _from_addr)
msg['to'] = format_addr('收件人小呵呵 <%s>' % to_addr)
msg['subject'] = Header('邮件标题嘿嘿嘿', 'utf-8')

server = smtplib.SMTP(_smtp_server, 25)
server.starttls()
server.set_debuglevel(1)
server.login(_from_addr, _password)
server.sendmail(_from_addr, [to_addr], msg.as_string())
server.quit()
