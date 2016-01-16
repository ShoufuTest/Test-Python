#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-01-16
# @Author  : Shoufu (gyming@outlook.com)
# @Version : 2.7.6

from wsgiref.simple_server import make_server
from wsgi_hello import *

httpd = make_server('', 8888, application)  # 创建一个服务器，IP地址为空，端口是8888，处理函数是application
print 'Serving HTTP on port 8888'
httpd.serve_forever()
