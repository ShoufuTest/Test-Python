#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-01-09
# @Author  : Shoufu (gyming@outlook.com)
# @Version : 2.7.6

import BeautifulSoup

url = 'http://news.ifeng.com/a/20160109/47006234_0.shtml'

html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""

code = BeautifulSoup(url)

print code.prettify()