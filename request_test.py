#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-01-09
# @Author  : Shoufu (gyming@outlook.com)
# @Version : 2.7.6

import requests
from bs4 import BeautifulSoup
from HTMLParser import HTMLParser

html_parser = HTMLParser()
url = 'http://news.sina.com.cn/c/2016-01-09/doc-ifxnkvtn9678626.shtml'

r = requests.get(url)
r.encoding = 'utf-8'
print 'encoding:', r.encoding


text =  html_parser.unescape(r.text)
soup = BeautifulSoup(text)
for item in soup.p:
    print item