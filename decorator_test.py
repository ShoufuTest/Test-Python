#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-02-15
# @Author  : Shoufu (gyming@outlook.com)
# @Version : 2.7.6


from gevent import monkey

monkey.patch_socket()
import gevent
import time
import requests
import Queue

url_queue = Queue.Queue()


def print_time(function):
    def wrapper(*args, **kw):
        start_time = time.time()
        parameter = function(*args, **kw)
        end_time = time.time()
        print 'Run time:{time}'.format(time=start_time - end_time)
        return parameter

    return wrapper


def host(addr):
    def decorator(func):
        def wrapper(args=None):
            if isinstance(args, list):
                print 'list:', args
            elif isinstance(args, str):
                print 'Str:', args
            elif not args:
                print 'None!'
            else:
                print type(args)
            print
            print 'IP Address is {addr}'.format(addr=addr)
            url = 'http://news.sina.com.cn'
            print 'Get url %s from queue.' % url
            print 'Push url to the function.\n'
            parameter = func(url)
            print 'Get the url from worker: %s' % parameter
            print 'Push the url to queue.'
            return parameter

        return wrapper

    return decorator


@host('192.168.11.1')
def f(url):
    print('GET: %s' % url)
    resp = requests.get(url)
    data = resp.text
    print('%d bytes received from %s.' % (len(data), url))
    print 'Saving the data.'
    print 'Return the url.\n'
    return url


a = f(['https://www.python.org/', 'https://www.qq.com/'])
print 'a:', a
