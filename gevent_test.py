#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-01-16
# @Author  : Shoufu (gyming@outlook.com)
# @Version : 2.7.6

from gevent import monkey; monkey.patch_socket()
import gevent

import urllib2
import requests

def f(url):
    print('GET: %s' % url)
    resp = urllib2.urlopen(url)
    data = resp.read()
    print('%d bytes received from %s.' % (len(data), url))
#
gevent.joinall([
        gevent.spawn(f, 'https://www.python.org/'),
        gevent.spawn(f, 'https://www.baidu.com/'),
        gevent.spawn(f, 'https://www.qq.com/'),
])

# text = requests.get('https://www.python.org/')
# print len(text)
f('https://www.baidu.com/')