#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-02-06
# @Author  : Shoufu (gyming@outlook.com)
# @Version : 2.7.6

from multiprocessing.managers import BaseManager


class QueueManager(BaseManager):
    pass


QueueManager.register('get_url_queue')
QueueManager.register('get_json_queue')


def host(addr):
    print 'Connect to server %s...' % addr
    worker = QueueManager(address=(addr, 5000), authkey='heheda')
    worker.connect()

    url_queue = worker.get_url_queue()
    finished_url_queue = worker.get_json_queue()

    def decorator(func):
        def wrapper(args=None):
            if isinstance(args, list):
                for url in args:
                    url_queue.put(url)
            elif isinstance(args, str):
                url_queue.put(args)
            while not url_queue.empty():
                if url_queue.qsize() >= 10:
                    urllist = [url_queue.get() for i in range(10)]
                else:
                    urllist = [url_queue.get() for i in range(url_queue.qsize())]
                finished_urllist = [func(url) for url in urllist]
                for url in finished_urllist:
                    finished_url_queue.put(url)

            return func

        return wrapper

    return decorator


@host('127.0.0.1')
def f(num):
    return '{num} * {num} is {result}'.format(num=num, result=num * num)



f([1, 2, 3, 4, 5])
