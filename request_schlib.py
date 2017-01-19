#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-01-25
# @Author  : Shoufu
# @Version : 2.7.6

import re
import requests
from HTMLParser import HTMLParser


hParser = HTMLParser()
liburl = 'http://opac.gdufs.edu.cn:8991/F'

lib_code = requests.get(liburl).text
login_url = re.findall(
    '<a href="(.*?)" class="blue" title="输入用户名和密码">', lib_code)[0]

post_data = {
    'func': 'login-session',
    'login_source': 'bor-info',
    'bor_id': '20131003443',
    'bor_verification': '888888',
    'bor_library': 'GWD50'
}

logined_code = requests.post(login_url, data=post_data).text
book_history_url = re.findall(
    'http:.*?func=bor-history-loan&adm_library=GWD50', logined_code)[0]

host_url = requests.get(book_history_url)
host_url.encoding='utf-8'
host_code = host_url.text
name = re.findall(u'管理库 - (.*?)的单册借阅历史列表', host_code)
if not name:
    print '老大！这逗逼没借过书！'
else:
    print name[0]

author = []
book = []
borrow_list = re.findall('target=_blank>(.*?)</a>', host_code)
for i in range(len(borrow_list)):
    if i%2 == 0:
        author.append(borrow_list[i])
    else:
        book.append(borrow_list[i])

# for item in author:
#     print item
for i in range(len(author)):
    print '%s.%s %s' % (i+1, author, book)
