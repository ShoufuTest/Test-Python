#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-01-16
# @Author  : Shoufu (gyming@outlook.com)
# @Version : 2.7.6

def application(environ, start_response):
    start_response('200 ok', [('Content-Type', 'text/html')])
    return '<h1>Hello, %s!</h1>' % (environ['PATH_INFO'][1:] or 'Web')