#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-01-09
# @Author  : Shoufu (gyming@outlook.com)
# @Version : 2.7.6

import re
import json
import requests
from HTMLParser import HTMLParser

html_parser = HTMLParser()
url = 'http://mp.weixin.qq.com/s?timestamp=1463119158&src=3&ver=1&signature=eAQEEXW5zsK6jQQzdXI9KhS38dgK02DueXaubu4XfG1khSMQupvPiUNEuFrrxif6De8MX6J46mULWDBjaQwBMxBLuiIcMmj7xG4Z39b99SdfltcLgWRstGvd8r4*xoX2b8s*mVshhuEPBtx1wkO*awHnXvq9WgAe3t-emHAK0QE='

r = requests.get(url)
r.encoding = 'utf-8'
print 'encoding:', r.encoding
print r.headers

content = ''
text = html_parser.unescape(r.text).encode('utf-8')
# print text

sg_data = re.findall('window.sg_data=([\\s\\S]*)seajs.use', text)[0]
src = re.findall('src:"(.*?)"', sg_data)[0]
ver = re.findall('ver:"(.*?)"', sg_data)[0]
timestamp = re.findall('timestamp:"(.*?)"', sg_data)[0]
signature = re.findall('signature:"(.*?)"', sg_data)[0]

data = {
    'src': src,
    'ver': ver,
    'timestamp': timestamp,
    'signature': signature
}
print data

url = 'http://mp.weixin.qq.com/mp/getcomment?src={0}&ver={1}&timestamp={2}&signature={3}'.format(
    src, ver, timestamp, signature)
r2 = requests.get(url)
print r2.text


def fetch(pageCode):
    sg_data = re.findall('window.sg_data=([\\s\\S]*)seajs.use', pageCode)[0]
    src = re.findall('src:"(.*?)"', sg_data)[0]
    ver = re.findall('ver:"(.*?)"', sg_data)[0]
    timestamp = re.findall('timestamp:"(.*?)"', sg_data)[0]
    signature = re.findall('signature:"(.*?)"', sg_data)[0]

    return {
        'src': src,
        'ver': ver,
        'timestamp': timestamp,
        'signature': signature
    }


def get_num(url):
    r = requests.get(url)
    sg_data = fetch(r.text)
    comment_url = 'http://mp.weixin.qq.com/mp/getcomment?src={0}&ver={1}&timestamp={2}&signature={3}'.format(
        src, ver, timestamp, signature)
    data_str = requests.get(comment_url).text
    data = json.loads(data_str)
    return {
        'like_num':data['like_num'],
        'read_num':data['read_num'],
    }
