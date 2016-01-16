#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-01-15
# @Author  : Shoufu (gyming@outlook.com)
# @Version : 2.7.6


email = 'gyming2015@163.com'
password = 'koucuhoezmipgmre'
pop3_server = 'pop.163.com'

import poplib

server = poplib.POP3(pop3_server)  # 连接到POP3服务器
server.set_debuglevel(1)  # 可以打开或关闭调试信息
print server.getwelcome()  # 可选:打印POP3服务器的欢迎文字

# 身份认证:
server.user(email)
server.pass_(password)
print 'Message: %s, Size: %s' % server.stat()  # stat()返回邮件数量和占用空间

resp, mails, octets = server.list()  # list()返回所有邮件的编号
index = len(mails)  # 获取最新一封邮件, 注意索引号从1开始
resp, lines, octets = server.retr(index)  # lines存储了邮件的原始文本的每一行
msg_content = '\n'.join(lines)  # 可以获得整个邮件的原始文本
# server.dele(index) # 可以根据邮件索引号直接从服务器删除邮件

import email
from email.parser import Parser
from email.header import decode_header
from email.utils import parseaddr

msg = Parser().parsestr(msg_content)  # 只需要一行代码就可以把邮件内容解析为Message对象


# 但是这个Message对象本身可能包含嵌套的其他MIMEBase对象，嵌套可能还不止一层。
# 所以要递归地打印出Message对象的层次结构：
def print_info(msg, indent=0):  # indent用于缩进显示
    if indent == 0:
        for header in ['From', 'To', 'Subject']:  # 邮件的From, To, Subject存在于根对象上
            value = msg.get(header, '')
            if value:
                if header == 'Subject':
                    value = decode_str(value)  # 需要解码Subject字符串
                else:
                    hdr, addr = parseaddr(value)  # 需要解码Email地址
                    name = decode_str(hdr)  # decode_str()方法在下面
                    value = '%s <%s>' % (name, addr)
                print '%s%s: %s' % (' ' * indent, header, value)
    if (msg.is_multipart()):
        parts = msg.get_payload()  # 如果邮件对象是一个MIMEMultipart, get_payload()返回list，包含所有的子对象
        for n, part in enumerate(parts):
            print '%spart %s' % (' ' * indent, n)
            print '%s------------------' % (' ' * indent)
            print_info(part, indent + 1)  # 递归打印每一个子对象
    else:
        # 邮件对象不是一个MIMEMultipart, 就根据content_type判断
        content_type = msg.get_content_type()
        if content_type == 'text/plain' or content_type == 'text/html':
            content = msg.get_payload(decode=True)  # 纯文本或HTML内容
            charset = guess_charset(msg)  # 要检测文本编码，方法在下面
            if charset:
                content = content.decode(charset)
            print '%sText: %s' % (' ' * indent, content + '...')
        else:
            print '%sAttachment: %s' % (' ' * indent, content_type)  # 不是文本,作为附件处理


def decode_str(s):  # 邮件的Subject或者Email中包含的名字都是经过编码后的str，要正常显示，就必须decode：
    value, charset = decode_header(s)[0]
    if charset:
        value = value.decode(charset)
    return value


def guess_charset(msg):  # 文本邮件的内容也是str，还需要检测编码，否则，非UTF-8编码的邮件都无法正常显示：
    charset = msg.get_charset()  # 先从msg对象获取编码
    if charset is None:
        content_type = msg.get('Content-type', '').lower()  # 如果获取不到，再从Content-Type字段获取
        pos = content_type.find('charset=')
        if pos >= 0:
            charset = content_type[pos + 8:].strip()
    return charset


print_info(msg)
server.quit()
